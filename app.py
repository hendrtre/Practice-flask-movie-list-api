from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello my baby, hello my darling, its a bright new wooooorrrrlllldd!</p><p>Hello, World!</p>"

if __name__ == "__main__":
    app.debug = True
    app.run()