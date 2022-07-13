import os
import csv
from flask import Flask, redirect, render_template, send_from_directory, request

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/submit_contact', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        data = request.form.to_dict()
        write_to_file(data)
        # write_to_csv(data)
        return redirect('tq.html')
    else:
        return 'Something went wrong!'

def write_to_file(data):
    with open('database.txt', mode='a') as file_db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = file_db.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as csv_db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(csv_db, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow ([email, subject, message])