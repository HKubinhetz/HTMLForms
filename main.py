from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def post_form():
    form_info = request.form.to_dict()
    print(f"Data: {form_info}")
    return render_template('login.html', data=form_info)


if __name__ == "__main__":
    app.run(debug=True)

