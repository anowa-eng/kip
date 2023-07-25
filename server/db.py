from pathlib import Path
import sqlite3

db_path = Path(__file__).parent / 'db.sqlite3'
def init():
    Path.touch(db_path)
    cursor = sqlite3.connect(db_path)
    users_table = '''
    CREATE TABLE IF NOT EXISTS Users (
        ID int NOT NULL PRIMARY KEY,
        Username varchar(255) NOT NULL,
        Password text NOT NULL
    );
    '''
    repositories_table = '''
    CREATE TABLE IF NOT EXISTS Repositories (
        ID int NOT NULL PRIMARY KEY,
        FullRepositoryName text NOT NULL,
        AuthorUsername varchar(255),
        RepositoryName varchar(255),
        ModelFilePath text,
        FOREIGN KEY (AuthorUsername) REFERENCES Users(Username)
    );
    '''
    cursor.execute(users_table)
    cursor.execute(repositories_table)
