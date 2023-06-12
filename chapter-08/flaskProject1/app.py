from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
