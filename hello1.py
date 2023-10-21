from flask import Flask, Request, jsonify, render_template

app = Flask(__name__)

DESIGNS = [
    {
        'id': 1,
        'title': 'WOTM',
        'description': "In today's digital age, the demand for faster and more reliable communication technologies "
                       "has reached unprecedented levels. From the early days of basic voice calls to the era of "
                       "mobile broadband, each generation of wireless communication has brought significant "
                       "advancements. However, as the world becomes increasingly connected and data-intensive "
                       "applications continue to emerge, there is a pressing need for a transformative technology "
                       "that can meet the demands of the future. This is where 5G technology comes into play.",

    },
    {
        'id': 2,
        'title': 'FAWC',
        'description': "In today's digital age, the demand for faster and more reliable communication technologies "
                       "has reached unprecedented levels. From the early days of basic voice calls to the era of "
                       "mobile broadband, each generation of wireless communication has brought significant "
                       "advancements. However, as the world becomes increasingly connected and data-intensive "
                       "applications continue to emerge, there is a pressing need for a transformative technology "
                       "that can meet the demands of the future. This is where 5G technology comes into play.",

    },
    {
        'id': 3,
        'title': 'TECHYFIRM',
        'description': "In today's digital age, the demand for faster and more reliable communication technologies "
                       "has reached unprecedented levels. From the early days of basic voice calls to the era of "
                       "mobile broadband, each generation of wireless communication has brought significant "
                       "advancements. However, as the world becomes increasingly connected and data-intensive "
                       "applications continue to emerge, there is a pressing need for a transformative technology "
                       "that can meet the demands of the future. This is where 5G technology comes into play.",

    }
]

@app.route('/')
def index():
    return render_template('home.html', designs=DESIGNS, company_name="TechyFirm")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
