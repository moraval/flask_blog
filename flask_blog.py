from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9975046c1e9cac3f0fc17636d0b29866'

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Hi {form.email.data}, you're logged in!", 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
