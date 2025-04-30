from tkinter import image_names

from flask import Flask, render_template, request, url_for, redirect
import csv

from jinja2.lexer import newline_re

# from markupsafe import escape
# import sys
# import pathlib

app = Flask(__name__)
print(app)
@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(page_name)
#
# @app.route('/index.html')
# def index():
#     return render_template('./index.html')
#
# @app.route('/works.html')
# def works():
#     return render_template('./works.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('./about.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        messsage = data["message"]
        file = database.write(f'\n{email},{subject},{messsage}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        messsage = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', lineterminator='\n', quotechar='|', quoting=csv.QUOTE_NONE)
        csv_writer.writerow([email,subject,messsage])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Invalid submition'



# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, Debug=True)