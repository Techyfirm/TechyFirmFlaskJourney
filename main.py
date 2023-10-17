from datetime import datetime

from flask import Flask, jsonify, request

from flask.ext.

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Retrieve current day and UTC time here
    current_day = datetime.date('current_day')
    utc_time = datetime.utcnow('utc_time')
    # Generate GitHub URLs based on input data
    github_file_url = 
    # Build JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
