from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    x = -2
    y = 5 * x + 7
    return render_template("ex1.html", x=x, y=y)

if __name__ == "__main__":
    app.run(debug=True)