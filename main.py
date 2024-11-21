
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5



class Myform(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(message='@,. are must', granular_message=False,
                                                                         check_deliverability=False,
                                                                         allow_smtputf8=True, allow_empty_local=False)])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8, message=None)])
    submit = SubmitField(label='Login')


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "hello21102004"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form_obj = Myform()
    if form_obj.validate_on_submit():
        if form_obj.email.data == "pragadajayasree@gmail.com" and form_obj.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form_obj)


if __name__ == '__main__':
    app.run(debug=True)
