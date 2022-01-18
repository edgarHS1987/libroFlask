from flask import request
from flask import make_response
from flask import Flask,render_template
from flask import redirect
from flask import abort


app = Flask(__name__)

@app.route('/login/<user>')
def login(user):
    return render_template('login.html',usuario=user)


@app.route('/')
def index():
    response = make_response('<h2>test</h2>')
    response.delete_cookie('cookieEdgar')
    return response


@app.route('/user/<name>')
def user(name):
    return '<h1> primera app con flask, pasamos un parametro {} </h1>'.format(name)

@app.route('/user/<int:idUser>')
def user2(idUser):
    parametroURL = str(idUser)
    return '<h1> funcion con usuario de tipo numerico, pasamos un parametro {} </h1>'.format(parametroURL)

@app.route('/test')
def test():
    user_agent = request.headers.get("User-Agent")
    return '<p>regreso esto , {}</p>'.format(user_agent)

@app.route('/redi')
def redi():
    return redirect('https://www.google.com/')

@app.route('/abortar/<id>')
def abortar(id):
    user = 'edgar123'
    if not user:
        abort(404)
    return '<h1>hola, {}</h1>'.format(user)

