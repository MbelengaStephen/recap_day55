from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b> {function()} </b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em> {function()} </em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u> {function()} </u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center;'>Hello, World!</h1>"\
           "<p> This is a paragraph</p>"\
           "<img src='https://media4.giphy.com/media/uWYjSbkIE2XIMIc7gh/giphy.gif?cid=ecf05e47cj07s44vkoyon5ofs1uhzvoi6ktpjih207jxhm0b&rid=giphy.gif&ct=g'>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye Mbelenga!</b></em>"


@app.route("/<name>/<int:number>")
def user(name, number):
    return f"Hello {name} you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
