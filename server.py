from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)
app.secret_key = 'Dojo survey'
@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/process', methods = ['post'])
def submit_info():
    print(request.form)
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['language']= request.form['language']
    session['comment']= request.form['comment']
    return redirect("/results")

@app.route('/results')
def result_info():
    print(request.form)
    return render_template('results.html')
if __name__ =="__main__":
    app.run(debug=True)

