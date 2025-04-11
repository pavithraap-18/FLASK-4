from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@example.com' and form.password.data == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
