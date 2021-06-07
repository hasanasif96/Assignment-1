# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:57:23 2021

@author: Hasan
"""

import flask
from flask import request, jsonify
import pandas as pd

df=pd.read_csv("C:\\Users\\Hasan\\Final_df.csv") 


app = flask.Flask(__name__)




@app.route('/check', methods=['POST','GET'])
def entity_check():
    
    # Check if an ID was provided in the URL.
    if 'text' in request.args:
        text = str(request.args['text'])
        print(text)

    # use for loop to iterate over the dataframe and check if input item is in City or person column
    #if any record foound then loops break
    for line in df.Person:
        if line == text:
            result="Person"
            break
        else:
            result="city"

    return jsonify(input_text= text,result=result)



if __name__ == '__main__':
	app.run(debug=True)