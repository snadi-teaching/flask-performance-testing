from flask import Flask, render_template
import os


app = Flask(__name__)


BACKEND_URL = "http://localhost:5000"


@app.route("/students")
def students():
    return render_template("create_student.html", backend_url=BACKEND_URL)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
