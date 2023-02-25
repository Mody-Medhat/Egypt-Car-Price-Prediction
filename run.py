import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import joblib
import Preprocess

# Load The Model
XGB_model = joblib.load('XGB.pkl')

# Read The Data
car = pd.read_csv('Hatla2ee-Egypt-Used-Car-V5.csv')

# add new columns
car['Brand'] = car['Brand'].str.replace(' ', '-')
car["Brand-Model"] = car['Brand'].astype(str) + " " + car["Model"]
car["Brand-Fule"] = car['Brand'].astype(str) + " " + car["Fule"].astype(str)
car["Brand-Body"] = car['Brand-Model'].astype(str) + " " + car["Body"].astype(str)

# Intialize the Flask APP
app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    brands = sorted(car['Brand'].unique())
    models = sorted(car['Brand-Model'].unique())
    #city = sorted(car['City'].unique())
    colors = sorted(car['Color'].unique())

    vehicle_styles = sorted(car['Brand-Body'].unique())
    car_styles = sorted(car['Body'].unique())
    fule_types = sorted(car['Brand-Fule'].unique())
    Engine_Fule_Types = sorted(car['Fule'].astype(str).unique())
    
    brands.insert(0, 'Select Brand...')
    return render_template('index.html', 
                           brands=brands,
                           models=models,
                           #city = city,
                           colors = colors,
                           vehicle_styles=vehicle_styles,
                           fule_types=fule_types,
                           Engine_Fule_Types=Engine_Fule_Types,
                           car_styles=car_styles,)


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    brand =  request.form['brand']
    brand  = brand.replace('-', ' ')
    try:    
        model =  request.form['model']
        model = model.split(' ', 1)[1]
        
        body =  request.form['vehicle_style']
        transmission =  request.form['Transmission']
        fule =  request.form['fule']
    except KeyError:
        meg = 'There Is An Empty Field Please Recheck The Data!!'
        return meg 
    try:
        year = int(request.form['year'])
        engine_cc =  int(request.form['engine_cc'])
        kilometers_Driven =  float(request.form['kilometers_Driven'])
    except ValueError:
        meg = 'There Is An Empty Field Please Recheck The Data!!'
        return meg    
    color =  request.form['color']
    #city =  request.form['city']

    data = {'Brand': brand,
                         'Model': model,
                         'Body': body,
                         'Transmission': transmission,
                         'Year': year,
                         'Fule': fule,
                         'Engine_CC': engine_cc,
                         'Kilometers_Driven': kilometers_Driven,
                         'Color': color,
                         }
    
    final_data = Preprocess.preprossecing(data)
    print('#'*200)
    print (final_data)
    print('#'*100)

    prediction = XGB_model.predict(final_data)
    #price = np.expm1(prediction)*1000 
    prediction_price = '{:.0f}'.format(prediction[0])
    #prediction_price = prediction[0]
    #prediction_price = prediction_price.astype(int)

    print(prediction_price) 

    return prediction_price + ' EGP'

# Run the App from the Terminal
if __name__ == '__main__':
    # app.run(debug=True,host='192.168.1.111',port=5000)
    app.run(port=8080, debug=True)


