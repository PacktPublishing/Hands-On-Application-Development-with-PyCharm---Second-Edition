from flask import Flask, render_template, request, make_response

app = Flask(__name__)
library_data = list()

library_data.append({"python_library": "Flask",
                     "description": "An unopinionated web framework",
                     "rating": 5,
                     "url": "https://pypi.org/project/Flask"})
library_data.append({"python_library": "Jinja2",
                     "description": "Templating library",
                     "rating": 3,
                     "url": "https://pypi.org/project/Jinja2"})


@app.route('/', methods=['GET', 'POST'])
def root():  # put application's code here
    return render_template("index.html", library_data=library_data)


if __name__ == '__main__':
    app.run()
