from flask import Flask, render_template, url_for, request, redirect, session
app = Flask(__name__)

app.config ['SECRET_KEY'] = '97d6faba210898c5b2ee478c'

@app.route('/')
@app.route('/home')                  
def index():
    if 'click' not in session:
        session['click'] = 0
    else:
        session['click'] += 1
    return render_template('index.html')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    