from flask import Flask, session, render_template, request, redirect, g
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__)) #the location of the file
UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER, 'static', 'upload') 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.secret_key = b'should be a secret'

users_db = {
    'jimmy': {'uid': 'jimmy', 'password': 'abcde', 'name': 'Jimmy Huang', 'email': 'jimmy@test.com'},
    'leuk': {'uid': 'leuk', 'password': 'abcde', 'name': 'leuk', 'email': 'leuk@test.com'} 
}

items_db = [{
    'item_id': 0,
    'uid': 'jimmy',
    'name': 'jjdn',
    'price': 150000000000000.0,
    'desc': 'hi',
    'filename':'BEST-PROGRAMMING-LANGUAGES.png'
},
    {
    'item_id': 1,
    'uid': 'jimmy',
    'name': 'Zhuge Liang',
    'price': 150000000000000.0,
    'desc': 'This is a person...',
    'filename':'zhu_ge_liang.jpg'
},
    {
    'item_id': 2,
    'uid': 'leuk',
    'name': 'as',
    'price': 12.0,
    'desc': 'as',
    'filename':'BEST-PROGRAMMING-LANGUAGES.png'
    }
]

def get_user():
  user_id = session.get('user_id')
  print(user_id)
  if user_id:
    g.user = users_db.get(user_id)
  else:
    g.user = { 'uid': None, 'name': 'Guest' }

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    get_user()
    return render_template('home.html', user = g.user, items = items_db, user_map=users_db)

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

@app.route('/profile')
def profile():
    get_user()
    return render_template('profile.html', user = g.user)

@app.route('/uploadfiles', methods=['GET', 'POST'])
def uploadfiles():
    get_user()
    if not g.user['uid'] or not g.user:
        return redirect('/')
    

    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        desc = request.form.get('desc')
        if not name or not price or not desc:
            return 'invalid input' 

        filename = None
        if 'picture' in request.files:
            pic = request.files['picture']
            if pic and allowed_file(pic.filename):
                filename = secure_filename(pic.filename)
                pic.save(os.path.join(UPLOAD_FOLDER, filename))

        item_id = len(items_db)
        items_db.append({
            'item_id': item_id,
            'uid': g.user['uid'],
            'name': name,
            'price': float(price),
            'desc': desc,
            'filename': filename
        })
        return redirect('/')

    return render_template('uploadfiles.html', user = g.user)

@app.route('/item/<item_id>')
def itemView(item_id):
    get_user()
    item = None
    for it in items_db:
        if str(it['item_id']) == item_id:
            item = it
            break
    return render_template('detail.html', item = item, user=g.user)

@app.route('/myitems')
def myItems():
    get_user()
    items = [it for it in items_db if it['uid'] == g.user['uid']]
    return render_template('my-items.html', user = g.user, items = items)

