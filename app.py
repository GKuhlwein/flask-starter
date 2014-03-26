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

@app.route("/madlib", methods=["GET","POST"])
def madlib():
    if request.method == 'GET':
        return render_template('madlibs.html')
    elif request.method == 'POST':
        Madlib2=request.form['Madlib2']
        Madlib=request.form['Madlib']
        return render_template('madlibs.html',
                                Madlib=Madlib,
                                Madlib2=Madlib2)

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
        tip=float(request.form['tip'])
        tax=float(request.form['tax'])
        mealcost=float(request.form['mealcost'])
        mealplustax = mealcost * tax + mealcost * tip + mealcost
        finishtax = mealcost * tax
        mealplustip = mealcost * tip
        return render_template('newer.html',
                               tip=tip,
                               mealcost=mealcost,
                               tax=tax,
                               mealplustax=mealplustax,
                               finishtax = finishtax,
                               mealplustip = mealplustip)
                               
if __name__ == "__main__":
    app.run(debug=True)
