from flask import Flask,render_template
import platform
import sys
import datetime

app= Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/hello')
def  hello_page():
  return  "Hello World"

@app.route ('/tokyo')
def tokypage():
 return  "Good job" 

@app.route('/status')
def status():
    dt = str(datetime.datetime.now())
    os = platform.system()
    pyver = sys.version
    return render_template('status.html',
                           title='Status',
                           date=dt,
                           operating_system=os,
                           python_version=pyver)

app.run(host='0.0.0.0',port=81)

