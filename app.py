from flask import Flask, render_template, send_file, request, redirect, session
from helper import failure, get_address, best_route, get_url
from werkzeug.utils import secure_filename
import os
import sqlite3

# Configure application
app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
UPLOAD_FOLDER = '/Users/euchunkang/Desktop/CS50'
ALLOWED_EXTENSIONS = {'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "OptiRoute"

# create SQL connection to SQLite database
con = sqlite3.connect('optiroute.db')
db = con.cursor()

@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/preupload", methods=["GET", "POST"])
def preupload():
    if request.method == "GET":
        return render_template("preupload.html")

    if request.method == "POST":
        # handle startpoint and endpoint
        if not request.form.get("startpoint"):
            return failure("Enter Start Point.")
        if not request.form.get("endpoint"):
            return failure("Enter End Point.")
        session["startpoint"] = request.form.get("startpoint")
        session["endpoint"] = request.form.get("endpoint")
        return render_template("upload.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["GET","POST"])
def upload():
    if request.method == "GET":
        return failure("This page is not accessible yet!")

    if request.method == "POST":
        file = request.files['file']
        # check if file is uploaded
        fname = file.filename
        if 'file' not in request.files:
            return failure('No file part.')
        if fname == '':
            return failure("No selected file.")
        # check if file is xlsx
        if not fname.endswith(".xlsx"):
            return failure("Upload files of type .xlsx ONLY.")
        #download file into my folder
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        startpoint = str(session["startpoint"])
        endpoint = str(session["endpoint"])
        address_list = get_address(file)
        # get best route and sort addresses
        try:
            sequence = best_route(startpoint, endpoint, address_list)
        except:
            return failure("Invalid start/end point or invalid address in sheet.")
        sorted_addresses = []
        for i in sequence:
            for address in address_list:
                if address == address_list[i]:
                    sorted_addresses.append(address)
        # adding in startpoint and endpoint
        sorted_addresses.insert(0, startpoint)
        sorted_addresses.append(endpoint)
        #remove file after retrieving addresses
        os.remove("/Users/euchunkang/Desktop/CS50/" + fname)
        # get url to google maps
        final_url = get_url(sorted_addresses)
        return redirect(final_url)


@app.route("/download", methods=["GET", "POST"])
def download():
    template = "Address_Template.xlsx"
    return send_file(template, as_attachment=True)


@app.route("/preentry", methods=["GET", "POST"])
def preentry():
    if request.method == "GET":
        return render_template("preentry.html")

    if request.method == "POST":
        # handle startpoint and endpoint
        if not request.form.get("startpoint"):
            return failure("Enter Start Point.")
        if not request.form.get("endpoint"):
            return failure("Enter End Point.")
        session["startpoint"] = request.form.get("startpoint")
        session["endpoint"] = request.form.get("endpoint")
        session["nloc"] = request.form.get("nloc")
        return render_template("entry.html", nloc=session["nloc"])


@app.route("/entry", methods=["POST"])
def entry():

    if request.method == "POST":
        address_list = []
        for i in range(1,int(session["nloc"])+1):
            address_list.append(request.form.get("location-"+str(i)))
        print(address_list)
        # get best route and sort addresses
        try:
            sequence = best_route(session["startpoint"], session["endpoint"], address_list)
            print(sequence)
        except:
            return failure("Invalid start/end point or invalid address in entries.")
        sorted_addresses = []
        for i in sequence:
            for address in address_list:
                if address == address_list[i]:
                    sorted_addresses.append(address)
        # adding in startpoint and endpoint
        sorted_addresses.insert(0, session["startpoint"])
        sorted_addresses.append(session["endpoint"])
        final_url = get_url(sorted_addresses)
        return redirect(final_url)

if __name__ == "__main__":
    app.run(debug=True)
