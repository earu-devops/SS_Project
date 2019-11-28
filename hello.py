#Import Modules
from flask import Flask

app = Flask(__name__)  #creating the Flask class Object
@app.route('/')  #route decorator defines the URL for mapping of the associated function

#Create Function
def home():
	return "hello, this is our first flask website"

#Main Program
if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0')  #Run the application
