from flask import Flask, render_template, request
import pyspark

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TESTING'] = True

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/", methods=['GET', 'POST'])
def index():
    if "submit" in request.form:
        author = request.form['date-start']

        # PySpark Query Here

        # returnvalue = result
        return render_template("index.html", returnvalue=str(request.form['date-start']))

    return render_template("index.html")
