from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
    # return "Hello world"

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/edit",methods={"GET","POST"})
# def edit():
#     if(request.method == "POST"):
#         print("reeeeeeqqqqq",request.form)
#         return render_template("index.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        print("Form data:", request.form)
        # Add your logic to handle the form data
        return render_template("about.html")  # Example response
    else:
        # Add logic for GET requests if needed
        return "Edit page"

# app.run(debug = True,port=5001)
if __name__ == "__main__":
    app.run(debug=True, port=5001)