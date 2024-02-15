from flask import Flask, render_template, request

app = Flask(__name__)
list = ["NO", "You sure?", "Last Chance!", "Pretty Please?", "NOOOOOO", "NEVER"]
counter = 0
numberOfNOs = 0

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("index.html", answer = list[counter])

@app.route('/no', methods = ['POST'])
def no():
    global counter
    global numberOfNOs
    numberOfNOs = numberOfNOs + 1
    counter = counter + 1
    if counter >= len(list):
        counter = 0
    return render_template("index.html", answer = list[counter])

@app.route('/yes', methods = ['POST'])
def yes():
    return render_template("yes.html", nos = numberOfNOs)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)