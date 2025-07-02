from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, DateField, SelectField, TextAreaField, EmailField,PasswordField
from wtforms.validators import EqualTo, DataRequired, InputRequired, Length



class RegisterForm(FlaskForm):
    username = StringField("Full Name", validators=[DataRequired(), Length(min = 3, max = 100)])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min = 3, max = 100)])
    confirm_password = PasswordField('confirm-Password', validators=[DataRequired(), EqualTo('password', message="Password Must Be Same")])
    submit = SubmitField('Register')



class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')



class JobForm(FlaskForm):
    company = StringField("Company", validators=[InputRequired()])
    role = StringField("Role", validators=[InputRequired()])
    link = StringField("Application Link")
    status = SelectField("Status", choices=[("Applied", "Applied"), ("Interview", "Interview"), ("Offered", "Offered"), ("Rejected", "Rejected")])
    deadline = DateField("Application Deadline")
    notes = TextAreaField("Notes")
    submit = SubmitField("Save")