from flask import Flask,request,jsonify
import util

app=Flask(__name__)

@app.route('/')
def function():
    response = {
        'str':util.fun()
    }
    return response

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*') # this make the API vulnerable to cross-site request forgery(CSRF)

    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.predict_price(location,total_sqft,bath,bhk)
    })
    response.headers.add('Access-Control-Allow-Origin','*') # this make the API vulnerable to cross-site request forgery(CSRF)
    return response


if (__name__=='__main__'):
    print('Starting flask server')
    util.load_data()
    app.run(debug=True)