from flask import Flask, render_template
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(DevConfig)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class Task(db.Model):
	__tablename__ = 'task'

	id = db.Column(db.Integer(), primary_key=True)
	taskname = db.Column(db.String(255))
	taskdescription = db.Column(db.String(255))

	def __init__(self, taskname):
		self.taskname = taskname

	def __repr__(self):
		return "<Task '{}'>".format(self.taskname)

@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run() 

