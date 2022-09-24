from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route("/sub" ,methods=['POST'])
def  submit():
    if request.method=='POST':
       name=request.form['user']
    return render_template('sub.html',n=name)

if __name__== '__main__':
    app.run()
