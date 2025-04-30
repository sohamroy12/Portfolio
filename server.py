from tkinter import image_names
from flask import Flask, render_template, request, url_for, redirect
import csv
from jinja2.lexer import newline_re

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(page_name)

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
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', lineterminator='\n', quotechar='|', quoting=csv.QUOTE_NONE)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Invalid submition'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, Debug=True)