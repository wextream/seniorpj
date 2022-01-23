from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def display_img():
    return render_template('index.html')


@app.route('/home')
def Hello():
    return 'Hello World'


if __name__ == "__main__":
    app.run(host='0.0.0.0')