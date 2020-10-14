from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "ala",
        "title": "my post",
        "content": "post content",
        "date": "today"
    },
    {
        "author": "spala",
        "title": "her post",
        "content": "the content",
        "date": "yesterday"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts, title="Home Home")


@app.route('/about')
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    app.run(debug=True)
