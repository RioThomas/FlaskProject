# https://github.com/RioThomas/FlaskProject.git

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    str_out = "<b>Convert celsius to fahrenheit:</b><br> " \
              "{} degrees Celsius equals {} degrees fahrenheit.0".format(celsius, fahrenheit)
    return str_out


if __name__ == '__main__':
    app.run()

