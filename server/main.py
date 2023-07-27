import sys
from pathlib import Path
from flask import Flask, request, jsonify
from flask_session import Session
import db

# Set up database
db.init()

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.get('/registry/<user>/<repo>')
def repository_download(user, repo):
    repository_path = Path(__file__).parent / f'registry/{user}/{repo}.kip'
    print(str(repository_path))
    if Path.exists(repository_path):
        with open(repository_path, 'r') as reader:
            response = app.make_response(reader.read())
            response.headers['Content-Type'] = 'application/octet-stream'
            response.headers['Content-Disposition'] = 'attachment'
            return response
    else:
        return jsonify({ 'error': 'Repository does not exist.' })
    
@app.post('/registry/<user>/<repo>')
def repository_create(user, repo):
    repository_path = Path(__file__).parent / f'registry/{user}/{repo}.kip'
    repository_path.write_bytes(request.files[0])
    cursor = db.create('Repositories', (f'{user}/{repo}', user, repo, ''))
    return jsonify(cursor.fetchone())

if __name__ == '__main__':
    app.run()