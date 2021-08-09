import os
from flask import Flask, render_template, request, jsonify

import marks

app = Flask(__name__)

@app.route("/predict", methods = ['POST'])
def predict():
    pred = mks_pdc = 0
    if request.method == "POST":
        hrs = request.form["hrs"]
        if hrs:
            mks_pdc = marks.marks_prediction(hrs)

    data = {'prediction': mks_pdc[0][0], 'hrs': hrs}
    return jsonify(data)

@app.route("/", methods = ['GET', 'POST'])
def hello():
    pred = mks_pdc = 0
    if request.method == "POST":
        hrs = request.form["hrs"]
        if hrs:
            mks_pdc = marks.marks_prediction(hrs)
            print(mks_pdc)

    return render_template("index.html", pred = mks_pdc)

#if __name__ == "__main__":
#    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
