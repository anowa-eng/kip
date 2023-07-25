import sys
from pathlib import Path
from flask import Flask
from flask_session import Session
import db

# Set up database
db.init()

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.get('/<user>/<repo>')
def repository_download(user, repo):
    repository_path = Path(__file__).parent / f'registry/{user}/{repo}.kip'
    with open(repository_path, 'r') as reader:
        response = app.make_response(reader.read())
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers['Content-Disposition'] = 'attachment'
        return response

if __name__ == '__main__':
    app.run()