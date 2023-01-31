from flask import Flask, render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField,IntegerField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

class Petform(FlaskForm):
    pid=IntegerField("Enter the pet id",validators=[DataRequired()])
    owner_name=StringField("Enter the owner name",validators=[DataRequired()])
    pet_name=StringField("Enter the pet name",validators=[DataRequired()])
    p_type=RadioField("Which animal type:", choices=[('dog',"Dog"),('cat',"Cats"),('other',"Others")])
    p_breed=StringField("Pet breed",validators=[DataRequired()])
    submit=SubmitField("Submit")


@app.route('/',methods= ['GET', 'POST'])
def index():
    form = Petform()
    if form.validate_on_submit():
        return render_template('petform.html', form=form)


if __name__ == "__main__":
    app.run()

