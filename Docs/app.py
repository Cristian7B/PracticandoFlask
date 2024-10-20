from flask import Flask

app = Flask(__name__)

@app.route("/route")
def home():
    return "Hello, World1!" 

if __name__ == "__main__":
    app.run()