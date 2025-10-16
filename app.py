from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur ma première application web en Python 🚀"

@app.route("/hello/<name>")
def hello(name):
    return f"Salut {name}, content de te voir ici ! 😄"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
