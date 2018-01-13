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




# Notes:
# In order to deploy a python application to the server, one must generate a flask app and a clean environment of python.
# How?
#
#Then, install (if needed the virtual env library by "pip install virtualenv")
# Then, create a root app (AppNo4....), inside add a resources folder (which will contain the css, html, .js, and a python script)
# then, create a module for .exe scripts by "python -m venv virtual" inside the root folder!
# then, install flask from root folder by using root's pip -
# e.g. virtual\Scripts\pip install Flask (and not just pip install flask)
# then, run the python script within the resources folder 
