""" we use flask to Develop websites. we do set FLASK_APP=main.py on the terminal, then we do flask run to run it  """
from flask import Flask
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return "hello_world, this is our website"

@app.route('/bad')
def badness():
    return "This is the the baddest"

@app.route('/Daniel')
def dan():
    return "This could only be God"
@app.route("/username/<name>/<password>")
def name(name, password):
    return f"Hello {name}, your password is {password} !"




if __name__ == "__main__":
    app.run()