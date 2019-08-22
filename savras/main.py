from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
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
    return '<h>Hello World!</h>'

if __name__ == '__main__':
    app.run() 

