from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "asdjsdjkacjksdc" #encrypts cookies and session data related to website, it can be whatever we want

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results", methods= ["POST", "GET"])
def results():
    integer = request.form.get("int_input")
    if request.method == "POST":
        return render_template("home.html", results = fizzbuzzFunc(int(integer)))


def fizzbuzzFunc(N:"int"):
    fizbuzStr = ""
    for i in range(1,N+1):
        if (i % 3 == 0) and (i % 5 == 0):
            fizbuzStr = fizbuzStr + str(i) + " ---> " + "FizzBuzz 🥂🐝" + "\n"
        elif (i % 3 == 0):
            fizbuzStr = fizbuzStr + str(i) + " ---> " + "Fizz 🥂" + "\n"
        elif (i % 5 == 0):
            fizbuzStr = fizbuzStr + str(i) + " ---> " + "Buzz 🐝" + "\n"
        else:
            fizbuzStr = fizbuzStr + str(i) + " ---> " + str(i) + "\n"
    return fizbuzStr


if __name__ == '__main__':
    app.run(debug=True)  # update flask server with changes we make