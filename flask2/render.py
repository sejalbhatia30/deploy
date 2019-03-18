import pandas as pd
import numpy as np
from splinter import Browser
from flask import Flask,render_template,url_for, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/render',methods = ['POST'])

def render_index():
    if request.method == 'POST':
        searche = request.form['nm']
        browser = Browser('chrome')
        browser.visit("https://amazon.in")
        search_bar = browser.find_by_id("twotabsearchtextbox")
        search_btn = browser.find_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
        search_bar.fill(searche)
        search_btn.click()
        element_path = '//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]'
        elements = browser.find_by_xpath(element_path)
        title = ['sejal']
        for element in elements:
            
            text = element.text
            title.append(text)
    
    
    return render_template('result.html',res=title)





