from flask import Flask
from fizzbuzz import FizzBuzz

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello world!"

@app.route('/fizzbuzz/<int:number>')
def fizzbuzz(number):
	fizzbuzz = FizzBuzz()
	return fizzbuzz.count(number)

if __name__ == '__main__':
	app.debug = True
	app.run('localhost', 3000, debug = True)