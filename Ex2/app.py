from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def student_info():
    return render_template('ex2.html')

if __name__ == '__main__':
    app.run(debug=True)