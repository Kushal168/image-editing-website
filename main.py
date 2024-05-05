from flask import Flask,render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'pdf','png', 'webp', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def hello_world():
    return render_template("index.html")
    # return "Hello world"

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        print("Form data:", request.form)
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        print("_____",request.files ,"++++",file.filename)
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print("=====>>>",file.filename)
            flash('No selected file')
            return "no fileeeee selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # processImage()
            return render_template("index.html")
    return  render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)