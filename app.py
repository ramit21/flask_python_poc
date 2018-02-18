#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:00:14 2018

@author: ramit21
"""
from flask import Flask, render_template, request, redirect, url_for
from models import *
app = Flask(__name__)#creating an instance of class Flask
#__name__ is a placeholder for the current module

@app.before_request
def before_request():
    print('Creating and connecting to DB')
    intialize_db()
    
@app.teardown_request   #app.after_request does not invoke in case of exception, but teardown does
def teardown_request(exception):
    print('Teardown: Closing DB [%s]'.format(exception))
    db.close()

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s' % name

@app.route('/double/<int:num>')
def double(num):
    return '%d' % (2*num)

@app.route('/')
def home():
    print('Render home page with saved posts')
    return render_template('home.html', posts = Post.select().order_by(Post.date.desc()))

@app.route('/new_post/')
def new_post():
    return render_template('new_post.html')

@app.route('/create/', methods = ['POST'])   # POST request
def create_post():
    print('Creating new Post')
    Post.create(
        title=request.form['title'],
        text=request.form['text']
    )
    #Redirect to funciton named homeabove. Can directly give hardcoded url as well
    return redirect(url_for('home'))

#return None from default route and see debug=True output. Should not be used in prod, 
#as client can can execute ython script directly in debug mode 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)