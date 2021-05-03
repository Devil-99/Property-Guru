import json
import pickle
import sklearn
import numpy as np

__location = None
__data_columns = None
__model = None

def fun():
    str="Server is running in util"
    return str

def predict_price(location,sqft,bath,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1

    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __location

def load_data():
    print('Loading Data...Start')
    global __data_columns
    global __location
    global __model

    with open("V:\Real-Estate Price Prediction\Server\datas\Columns.json",'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __location = __data_columns[3:]

    with open("V:\Real-Estate Price Prediction\Server\datas\Price_Detection_model.pickle",'rb') as f:
        __model = pickle.load(f)

    print('Loading Data...Done')

if (__name__=='__main__'):
    load_data()
    #get_location_names()
    print(predict_price('Indira Nagar',1000,2,2))
    print(predict_price('1st phase jp nagar',1000,2,2))
    print(predict_price('1st phase jp nagar',1000,3,3))