from flask import Flask, render_template

#Flask for the server, render_template for accessing html files in python
#instantiation
app=Flask(__name__)

#Annotation for a website
#port 5000 by default
@app.route('/')
#function name - only one function (can't have two "home" functions)
def home():
    # in order to render, a page must be under a "templates" folder
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__== "__main__":
    # on first place - if it's imported from Flask - it will always be "__main__",
    # otherwise - it'll be a "__script1__" for example
    app.run(debug=True)
