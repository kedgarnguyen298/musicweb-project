from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.methods == 'GET':
        return render_template('register.html')
    else:
        form = request.form
        email = form.email
        username = form.username
        password = form.password
        
        

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 