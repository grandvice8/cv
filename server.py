from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.today().year
    return render_template('index.html', year=year)

@app.route('/works')
def work():
    year = datetime.today().year
    return render_template("works.html", year=year)

if __name__ == "__main__":
    app.run(debug=True)
