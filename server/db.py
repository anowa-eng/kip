from pathlib import Path
import sqlite3

COLS = {
    'Users': 2,
    'Repositories': 4
}
TABLES = ('Users', 'Repositories')

db_path = Path(__file__).parent / 'db.sqlite3'
def init():
    Path.touch(db_path)
    connection = sqlite3.connect(db_path)
    users_table = '''
    CREATE TABLE IF NOT EXISTS Users (
        Username varchar(255) NOT NULL PRIMARY KEY,
        Password text NOT NULL
    );
    '''
    repositories_table = '''
    CREATE TABLE IF NOT EXISTS Repositories (
        FullRepositoryName text NOT NULL PRIMARY KEY,
        AuthorUsername varchar(255),
        RepositoryName varchar(255),
        ModelFilePath text,
        FOREIGN KEY (AuthorUsername) REFERENCES Users(Username)
    );
    '''
    connection.execute(users_table)
    connection.execute(repositories_table)
    connection.commit()

def create(table, values):
    connection = sqlite3.connect(db_path)
    stmt = f"INSERT INTO {table} VALUES ({', '.join('?' * COLS[table])})"
    return connection.execute(stmt, values)

def fetchpw(username):
    connection = sqlite3.connect(db_path)
    stmt = "SELECT Password FROM Users WHERE Username = ?"
    return connection.execute(stmt, (username,)).fetchone()[0]
