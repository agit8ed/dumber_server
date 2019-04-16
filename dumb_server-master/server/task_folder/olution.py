from flask import Flask, redirect, render_template
from login_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# http://127.0.0.1:8080/login
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and form.username.data == "test" and form.password.data == "test":
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    return "Success!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
