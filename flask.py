# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:04:10 2021

@author: samee
"""

from flask import Flask
from flask import jsonify
import numpy as np

application = Flask(__name__)

@application.route('/')
def hello():
        return 'Hello SAMEER\n'

@application.route('/random/<n>')
def randomvalues(n):
        values=np.random.randint(0,10,int(n))
        result={'values':values.tolist()}
        return jsonify(result)

if __name__=='__main__':
        application.run(debug=True)