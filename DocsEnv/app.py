from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/routeenv")
def env_test():
    return "Hello, World!"

@app.route("/nombre/<name>")
def nombre(name):
    return f"Hola {escape(name)}"

if __name__ == "__main__":
    app.run()