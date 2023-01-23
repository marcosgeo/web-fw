# app.py

from bumbo.api import API


app = API()


@app.route("/home")
def home(request, response):
    response.text = "\nHello from the HOME page\n\n"
    


@app.route("/about")
def about(request, response):
    response.text = "\nHello from the ABOUT page\n\n"


@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"\nHello, {name}\n\n"


@app.route("/sum/{num_1:d}/{num_2:d}")
def sum(request, response, num_1, num_2):
    total = int(num_1) + int(num_2)
    response.text = f"\n{num_1} + {num_2} = {total}\n\n"


