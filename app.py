from flask import Flask, jsonify

from libs.cases import get_covid_cases
from libs.timedate import getDate


app = Flask(__name__)


@app.route("/api/v1", methods=["GET"])
@app.route("/api/v1/<date>", methods=["GET"])
def index(date=None):
    if date is None:
        yesterday = getDate()
        cases = get_covid_cases(yesterday)
    else:
        cases = get_covid_cases(date)

    return jsonify({"total_cases": cases})


if __name__ == "__main__":
    app.run(debug=True)
