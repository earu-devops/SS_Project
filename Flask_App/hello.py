#Import Modules
from flask import Flask

app = Flask(__name__)  #creating the Flask class Object
@app.route('/')  #route decorator defines the URL

#Create Function
def home():
	return "hello, this is our first flask website"

#Main Program
if __name__ == '__main__':
	app.run(debug = True)  #Run the application
