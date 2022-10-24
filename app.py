from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('main.html')


@app.route('/prev')
def prev_method():
    return render_template('index.html')

@app.route('/route_name')
def next_method():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 