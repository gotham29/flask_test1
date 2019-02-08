#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 23:51:59 2019

@author: samuelheiserman
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"