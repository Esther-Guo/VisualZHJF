#encoding:utf-8


from flask import Flask,render_template
import config
import os
import json
#EG
import numpy as np
import pandas as pd
from IPython.display import HTML


app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/radar')
def radar():
    id = "201611580516"
    with open('data/info.json', encoding='utf-8') as json_file:
	    data = json.load(json_file)
    score = data[id]["score"]
    name = data[id]["name"]
    return render_template('radar.html',score = score,name = name)

@app.route('/zhexian')
def zhexian():
    A_data=[3.17, 3.75, 3.21, 3.46, 3.43, 3.31, 3.08, 3.61]
    B_data=[3.1, 3.00, 3.38, 3.01, 3.52, 3.87, 3.37, 3.85]
    return render_template('zhexian.html',A_data=A_data,B_data=B_data)

#EG
@app.route('/table')
def table():
    data = open('data/data.json',encoding='utf8').read()
    columns = ["stuid","name","classid","grade"]
    dat = json.loads(data)
    dic = {
        "stuid":[],
        "name":[],
        "classid":[],
        "grade":[]
    } 
    for stu in dat:
        dic['stuid'].append(stu['stuid'])
        dic['name'].append(stu[u'name'])
        dic['classid'].append(stu['classid'])
        dic['grade'].append(stu['grade'])
    df = pd.DataFrame(data = dic, columns = columns)
    convert = df.to_html(classes = 'table table-striped',border=None, justify=None)
    head = '''
        {% extends 'base.html' %}

        {% block title %}表格页面{% endblock %}

        {% block main %}

        <body style="height: 100%; margin: 0">
            <h4 style="text-align: left">学生成绩</h1>
            <div id="container" style="height: 100%">
        '''
    tail = '''
            </div>
            {% endblock %}
        '''
    with open('templates/table.html', 'w',encoding='utf8') as f:
        f.write(head)
        f.write(convert)
        f.write(tail)
    return render_template('table.html')



if __name__ == '__main__':
    app.run()