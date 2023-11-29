from flask import Flask, render_template

app = Flask(__name__)
POSTS = [{
    'id': 1,
    'title': 'Desktop Engineer',
    'location': 'San Francisco',
    'salary': 'MK2000'
}, {
    'id': 2,
    'title': 'Car Engineer',
    'location': 'Lilongwe',
    'salary': 'MK2100'
}, {
    'id': 3,
    'title': 'Blog Trespssser',
    'location': 'Miniland',
    'salary': 'MK2200'
}]


@app.route("/")
def hello_world():
  return render_template("index.html", posts=POSTS)


if __name__ == "__main__": app.run(host='0.0.0.0', debug=True)
