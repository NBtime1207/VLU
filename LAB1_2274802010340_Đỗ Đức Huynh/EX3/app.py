from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('ex3.html')

if __name__ == '__main__':
    app.run(debug=True)