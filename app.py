from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello", methods=["GET","POST"])
def example_form():
    if request.method == 'GET':
        return render_template('hello.html')
    elif request.method == 'POST':
        return render_template('greeting.html',
                               fullname=request.form['fullname'])
@app.route("/my-new-page", methods=["GET","POST"])
def my_new_function():
    print 'HELLO FROM MY NEW FUNCTION'
    if request.method == 'GET':
        return render_template('new-page.html')
    elif request.method == 'POST':
        return render_template('new.html',
                               fullname=request.form['fullname'])
    
    
@app.route("/new")
def new():
    return render_template('new.html')
	
@app.route("/tip", methods=["GET","POST"])
def tip():
    if request.method == 'GET':
        return render_template('newer.html')
    elif request.method == 'POST':
        return render_template('newer.html',
                               tip=request.form['tip'],
							   mealcost=request.form['mealcost'],
                               tax=request.form['tax'])

if __name__ == "__main__":
    app.run(debug=True)
