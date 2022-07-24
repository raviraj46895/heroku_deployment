
from flask import Flask, render_template, request
import numpy as np
import joblib

#initialise the app
app= Flask(__name__)
model= joblib.load(r'C:\Users\hp\OneDrive\Desktop\deployment\joblib\dib_79.pkl')

@app.route('/')
def hello_world():
    return render_template('dib.html')

@app.route('/predict',methods=['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    print(preg,plas,pres,skin,test,mass,pedi,age)

    #output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    output = np.array([[preg,plas,pres,skin,test,mass,pedi,age]])

    if output[0]==1:
        print('dibatic')
    else:
        print('not dibatic')

    return 'Form Submitted'
#run the app
app.run(debug=True)