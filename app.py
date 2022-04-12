# import importlib
from flask import Flask, redirect, url_for, render_template, jsonify, json
from EquityBulls import limited
from iifl import limitedIifl
from third import headings_links

app = Flask(__name__)  # define app

@app.route('/')  # path set
def home():
    return render_template('index.html')


@app.route('/equitybulls')  # path set
def EQ():
    return render_template('newsEquity.html', limited=limited)


@app.route('/iifl')  # path set
def iifl():
    return render_template('newsIifl.html', limitedIifl=limitedIifl)


@app.route('/livemint')  # path set
def livemint():
    return render_template('livemint.html', limited=headings_links)


@app.route('/predict')  # path set
def predict():
    return render_template('predict.html')


@app.route('/sentiment')  # path set
def sentiment():
    return render_template('sentiment.html')


@app.route('/display_candlestick')
def chart():
    return render_template('display_candlestick.html')


@app.route("/status")
def user(name):
    return jsonify({"msg": "api is running"})


# @app.route("/admin/")
# def admin():
#     return redirect(url_for("user", name="Admin"))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
