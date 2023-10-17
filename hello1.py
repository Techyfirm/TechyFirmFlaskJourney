from flask import Flask, Request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)