from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    interests = request.form.getlist('interests')

    return render_template('result.html', name=name, age=age, gender=gender, interests=interests)

if __name__ == '__main__':
    app.run(debug=True)
