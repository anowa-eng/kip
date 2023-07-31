from pathlib import Path
import sqlite3

COLS = {
    "Users": 2,
    "Repositories": 4
}
TABLES = ("Users", "Repositories")

db_path = Path(__file__).parent / "database.db"
def init():
    Path.touch(db_path)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    users_table = """
    CREATE TABLE IF NOT EXISTS Users (
        Username varchar(255) NOT NULL UNIQUE PRIMARY KEY,
        Password text NOT NULL
    );
    """
    repositories_table = """
    CREATE TABLE IF NOT EXISTS Repositories (
        FullRepositoryName text NOT NULL PRIMARY KEY,
        AuthorUsername varchar(255),
        RepositoryName varchar(255),
        ModelFilePath text,
        FOREIGN KEY (AuthorUsername) REFERENCES Users(Username)
    );
    """
    cursor.execute(users_table)
    cursor.execute(repositories_table)
    connection.commit()
    connection.close()

def create(table, values):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    placeholders = list(map(
        lambda n: "?",
        range(COLS[table])
    ))
    stmt = f"INSERT INTO {table} VALUES ({', '.join(placeholders)})"
    result_cursor = cursor.execute(stmt, values)
    connection.commit()
    return result_cursor

def fetchpw(username):
    cursor = sqlite3.connect(db_path).cursor()
    stmt = "SELECT Password FROM Users WHERE Username = ?"
    return cursor.execute(stmt, (username,)).fetchone()[0]

def user_exists_with_name(username):
    cursor = sqlite3.connect(db_path).cursor()
    stmt = "SELECT Username FROM Users WHERE Username = ?"
    existing_users_with_name = cursor.execute(stmt, (username,)).fetchall()
    return existing_users_with_name != []
