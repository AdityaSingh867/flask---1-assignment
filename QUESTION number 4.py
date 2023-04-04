from flask import Flask
from flask import request

apple = Flask(__name__)
@apple.route('/welcome')
def test():
    return '<h1>Welcome to ABC Corporation</h1>  Company Name: ABC Corporation , Location: India , Contact Detail: 999-999-9999'

if __name__=="__main__":
    apple.run(host="0.0.0.0")