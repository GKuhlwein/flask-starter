from flask import Flask, render_template, request
signup = Flask(__name__)

@signup.route("/", methods=["GET","POST"])
def su():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        return render_template('signup2.html',
                               lastname=request.form['lastname'],
                               firstname=request.form['firstname'])
@signup.route('/su2', methods=['GET','POST'])
def su2():
    if request.method == 'GET':
        return render_template('signup2.html')
 
@signup.route('/su3', methods=['GET','POST'])
def su3():
    if request.method == 'GET':
        return render_template('signup3.html')
    elif request.method == 'POST':
        return render_template('signup3.html',
                               Comment=request.form['Comment'])
                               
@signup.route('/su4', methods=['GET','POST'])
def su4():
    if request.method == 'GET':
        return render_template('signup4.html')
    elif request.method == 'POST':
        return render_template('signup4.html',
                               modify=request.form['modify'])
                               
if __name__ == "__main__":
    signup.run(debug=True)