from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guest.db'
db = SQLAlchemy(app)

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	comment = db.Column(db.String(1000))

@app.route('/')
def index():
	result = Comment.query.all()

	return render_template('index.html', result=result)

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']

	signature = Comment(name=name, comment=comment)
	db.session.add(signature)
	db.session.commit()

	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)