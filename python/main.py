import pandas as pd
import numpy as np
from utils.getdata import getdata, preprocessing

def retrain(params):
    '''
    for retrain
    '''
    data = getdata(params)

    data = preprocessing(data)

def predict():
    '''
    for predict
    '''

def kpi():
    '''
    calculate kpi
    '''


def main(params):

    retrain(params)

    return

if __name__ == '__main__':

    params = {
        "fab" : 'FAB12',
        "method" : "prediction"
    }

    main(params)

    predict()
