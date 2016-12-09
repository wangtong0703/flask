from flask import Flask, render_template, url_for
from flask import request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
	#user_agent = request.headers.get('User-Agent')
	#return '<h1>Hello World!</h1><p>Your browser is %s</p>' % user_agent
	return render_template('index.html',current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
	#return '<h1>Hello,%s!</h1>' % name,400
	return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

if __name__ == '__main__':
	#app.run(debug=True)
	manager.run()


