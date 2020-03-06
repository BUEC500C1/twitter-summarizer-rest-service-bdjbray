from flask import Flask, render_template, url_for,request
import cgi
import cgitb
import twitter
import os

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/hello', methods=['POST'])
def hello():
    the_name = request.form['user_name']
    print(the_name)
    cmdmulti="python twitter.py "+str(the_name)
    os.system(cmdmulti)
    return 'Thanks for usings! <br/> The tweets of %s have been collected! <br/> <a href="/">Back Home</a>' % (the_name)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)