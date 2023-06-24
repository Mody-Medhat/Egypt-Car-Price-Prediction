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
    
    brands.insert(0, 'Select Brand')
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

    prediction = XGB_model.predict(final_data)

    prediction_price = '{:.0f}'.format(prediction[0])
   
    def determine_price_range(predicted_price):
        ## https://tradingeconomics.com/egypt/core-inflation-rate#:~:text=Core%20Inflation%20Rate%20in%20Egypt%20averaged%2010.39%20percent%20from%202005,percent%20in%20July%20of%202020.
        inflation_percentage = 0.403  # 5% annual inflation rate
        base_market_fluctuation_percentage = 0.1  # 10% base market fluctuation

        # Adjust the predicted price for inflation
        predicted_price *= (1 + inflation_percentage)

        # Calculate the minimum and maximum price based on the predicted price
        min_price = predicted_price * (1 - base_market_fluctuation_percentage)
        max_price = predicted_price * (1 + base_market_fluctuation_percentage)

        # Adjust the price range difference based on the predicted price
        price_difference = max_price - min_price
        price_difference_threshold = 100000  # Adjust this threshold based on your market

        if price_difference > price_difference_threshold:
            min_price = predicted_price - (price_difference_threshold / 2)
            max_price = predicted_price + (price_difference_threshold / 2)

        price_range = {'min_price': round(min_price, 1) , 'max_price': round(max_price , 1)}

        return price_range

    price_range = determine_price_range(float(prediction_price))

    return price_range
# Run the App from the Terminal
if __name__ == '__main__':
    # app.run(debug=True,host='192.168.1.111',port=5000)
    app.run(port=8080, debug=True)


