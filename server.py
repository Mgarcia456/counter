from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = 'hello'
#     this route is foir my button that will add one to the counter everytime pressed
@app.route('/')
def counter(): 
    if 'count' not in session: session['count'] = 0
    else: session['count'] += 1
    return render_template("index.html")
#       this route will clear the counter/session back to zero
@app.route('/destroy_session')
def destroy_session(): 
    session.clear()
    return redirect('/')
#      this route is for the button that will add two instead of one
@app.route('/double_count')
def double_count():
    session['count'] += 1
    return redirect('/')
#         will add to the clicker the custom amount posetd on url by user
@app.route('/custom_count', methods=['POST'])
def custom_count():
    session['count'] += int(request.form['count'])-1
    return redirect('/')


if __name__ == "__main__": app.run(debug=True, port=5000)