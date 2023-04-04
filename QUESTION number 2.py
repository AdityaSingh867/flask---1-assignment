from flask import Flask
from flask import request

apple = Flask(__name__)

@apple.route('/file_')
def file_():
    return'<h1>Hello World!!</h1>'

if __name__=="__main__":
    apple.run(host="0.0.0.0")