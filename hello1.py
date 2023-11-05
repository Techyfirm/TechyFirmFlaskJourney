from flask import Flask, Request, jsonify, render_template

app = Flask(__name__)

DESIGNS = [
    {
        'id': 1,
        'title': 'WOTM',
        'description': "Some quick example text to build on the card title and make up the bulk of the card's content.",

    },
    {
        'id': 2,
        'title': 'FAWC',
        'description': "Some quick example text to build on the card title and make up the bulk of the card's content.",

    },
    {
        'id': 3,
        'title': 'TECHYFIRM',
        'description': "Some quick example text to build on the card title and make up the bulk of the card's content.",

    }
]


@app.route('/')
def index():
    return render_template('home.html', designs=DESIGNS, company_name="TechyFirm")


@app.route('/api/designs')
def design_list():
    return jsonify(DESIGNS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
