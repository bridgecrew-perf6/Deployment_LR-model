from urllib import request
from flask import Flask , render_template, request
import joblib
app = Flask(__name__)

#load the model
model=joblib.load("templates\Model\diabatic_80.pkl")

@app.route('/') # decorator
def home(): #function
    return render_template('home.html')

@app.route('/data', methods=['post'])
def data():
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')

    print(preg, plas, pres, skin, test, mass, pedi, age)

    result = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if result[0]==1:
        data = 'person is diabetic'
    else:
        data = 'person is not diabetic'


    return render_template('predict.html', data=data)

app.run() # should be always at the end

"""
http: hyper text transfer protocol
127.0.0.1 - ip address - localhost
:5000 - port
/ - route

http://127.0.0.1:5000/

""" 