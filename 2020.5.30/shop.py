from flask import Flask, session, render_template, request, redirect, g

app = Flask(__name__)

app.secret_key = b'should be a secret'

users_db = {
    'jimmy': {'uid': 'jimmy', 'password': 'abcde', 'name': 'Jimmy Huang', 'email': 'jimmy@test.com'}, 
}


def get_user():
  user_id = session.get('user_id')
  print(user_id)
  if user_id:
    g.user = users_db.get(user_id)
  else:
    g.user = { 'uid': None, 'name': 'Guest' }

@app.route('/')
def index():
    get_user()
    return render_template('home.html', user = g.user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        uid = request.form.get('uid')
        password = request.form.get('password')
        print(uid, password)

        if not uid or not password:
            return 'invalid input'
        
        user = users_db.get(uid)
        if not user:
            return 'User not found'

        if user.get('password') != password:
            return 'password error'

        session['user_id'] = uid

        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect('/')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uid = request.form.get('uid')
        password = request.form.get('password')
        uname = request.form.get('uname')
        email = request.form.get('email')
        print(uid, password)

        if not uid or not password or not uname or not email:
            return 'invalid input'
        
        user = users_db.get(uid)
        if user:
            return 'User already exists'

        users_db[uid] = {
            'uid': uid, 'password': password, 'name': uname, 'email': email
        }

        session['user_id'] = uid

        return redirect('/')
    return render_template('signup.html')


