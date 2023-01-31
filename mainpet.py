from wtforms import Form, BooleanField, StringField, validators, SubmitField, HiddenField
from flask_wtf import FlaskForm
from flask import render_template, Flask,redirect,url_for,request
import psycopg2
from form import owner
from db import Pet, DBconnection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' 

db = DBconnection()
db.connect_db()
try:
    db.create_table('pid','owner_name','p_name','ptype','p_breed',)
except Exception as ex:
    pass 
db.close()

@app.route('/')
def index():
    try:
        db.connect_db()
        pet_shop = db.select_result('pet_shop')
        db.close()
        return render_template('frontpage.html',pet_shop = pet_shop)
    except Exception as ex:
        msg = "An error has occured while showing result! : " + str(ex)
        return render_template('error.html',error = msg)
        

@app.route('/create',methods = ['GET','POST'])
def create():
    try:
        form = owner()
        if request.method == 'POST' and form.validate_on_submit():
            pid=form.pid.data
            owner_name = form.owner_name.data
            p_name=form.p_name.data
            p_type=form.p_type.data
            p_breed=form.p_breed.data
            db.connect_db()
            db.insert_db('pet_shop',pid,owner_name,p_name,p_type,p_breed)
            db.close()
            return  redirect(url_for('index'))
        return render_template('create.html',form = form)
    except Exception as e:
        error = "An error has occured while adding the data! : "+ str(e)
        return render_template('error.html',msg=error)

@app.route('/delete/')
def delete(ids):
    try:
        db.connect_db()
        db.delete_row('pet_shop',ids)
        db.close()
        return redirect(url_for('index'))
    except Exception as ex:
        error = "An error has occured while Deleting the data! : "+ str(ex)
        return render_template('error.html',msg=error)

@app.route('/edit/',methods = ['GET', 'POST'])
def edit(ids):
    try : 
        db.connect_db()
        pet_shop_row = db.select_row('pet_shop',ids)
        form = owner()
        form.owner_name.data = pet_shop_row[0][3]

        if request.method == 'POST' and form.   validate_on_submit():
            name = form.name.data
            pet_name = form.pet_name.data
            p_breed = form.p_breed.data

            db.connect_db()
            db.edit('pet_shop',pet_name,p_breed,owner_name,ids)
            db.close()
            return redirect(url_for('index'))   
        return render_template('change.html',form = form)
    except Exception as ex:
        error = "An error has occured while Editing the data! : "+ str(ex)
        return render_template('error.html',msg=error)

@app.route('/error/msg')
def error(msg):
    return render_template('error.html', error=msg)

if __name__ == '__main__':
    app.run(debug=True, port = 5500)