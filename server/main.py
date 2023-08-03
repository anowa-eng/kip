import bcrypt
from pathlib import Path
from flask import Flask, request, session, jsonify
from flask_session import Session
import db

# Set up database
db.init()

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.get('/registry/download/<user>/<repo>')
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
    
@app.post('/user/register')
def register_user():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        if db.user_exists_with_name(username):
            raise Exception('A user with the name already exists.')
        hashed_password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())
        if all([username, password]):
            cursor = db.create('Users', (username, hashed_password))
            return jsonify({ 'ok': True })
        else:
            raise Exception('Username and password are required.')
    except Exception as e:
        return jsonify({
            'ok': False,
            'error': str(e)
        })

@app.post('/user/login')
def login_user():
    try:
        username = request.form.get('username')
        password_attempt = request.form.get('password')
        if not all([username, password_attempt]):
            raise Exception('Username and password are required.')
        if not db.user_exists_with_name(username):
            raise Exception(f'User {username} does not exist.')
        user_password = db.fetchpw(username)
        encoded_password_attempt = password_attempt.encode('utf-8')
        if bcrypt.checkpw(encoded_password_attempt, user_password):
            session['logged_in_as'] = request.form.get('username')
            return jsonify({ 'ok': True })
        else: raise Exception('Incorrect password.')
    except Exception as e:
        return jsonify({
            'ok': False,
            'error': str(e)
        })

@app.post('/user/logout')
def logout_user():
    session['logged_in_as'] = None
    return jsonify({ 'ok': True })

@app.post(r'/registry/create/<repo>')
def repository_create(user, repo):
    repository_path = Path(__file__).parent / f'registry/{user}/{repo}.kip'
    request.files[0].save(repository_path)
    cursor = db.create('Repositories', (f'{user}/{repo}', user, repo, repository_path))
    return jsonify(cursor.fetchone())

if __name__ == '__main__':
    app.run()