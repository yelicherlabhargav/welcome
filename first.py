import flask,requests,json
import jinja2
from authlib.flask.client import OAuth
from flask import Flask, redirect, url_for, render_template, request, flash
from flask import Flask, redirect, url_for, request

app = flask.Flask(__name__)

@app.route("/")
def home_view():
    return "<p>hello</p>"

@app.route("/test")
def test():
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return render_template('demo.html',name=name)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request .method == 'POST':
        user = request.form['nm']
        return redirect (url_for('success',name = user))
    else:
        user = request.args.get('nm')
    return redirect(url_for('success',name = user))

    if __name__ == '__main__':
        app.run(debug = True)

@app.route("/abc")
def abc():
    return jsonify(
message="good test",
category="success",
data=data,
status=200
            )
