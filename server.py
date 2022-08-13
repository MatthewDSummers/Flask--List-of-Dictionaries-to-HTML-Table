from flask import Flask, render_template
app = Flask(__name__)

chars_info = [
        {'first_name' : 'Squall', 'last_name': 'Leonhart', 'age' : 17, 'height':'5\'10"'},
        {'first_name' : 'Rinoa', 'last_name': 'Heartilly', 'age' : 17, 'height':'5\'4"'},
        {'first_name' : 'Zell', 'last_name': 'Dincht', 'age' : 17, 'height':'5\'6"'},
        {'first_name' : 'Seifer', 'last_name': 'Almasy', 'age' : 18, 'height':'6\'2"'},
    ]

@app.route('/characters')
def render_chars():
    return render_template("index.html", chars_list=chars_info)

@app.route('/characters/<number>')
def frequency(number):
    num = int(number)
    return render_template("index.html", chars_list=chars_info, frequency = num)

if __name__=="__main__":
    app.run(debug=True)