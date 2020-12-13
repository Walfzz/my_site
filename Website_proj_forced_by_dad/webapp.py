from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author ': 'Dayan',
        'title': 'blog post 1',
        'content': 'first',
        'date_posted': '???'
    },
    {
        'author ': 'Dayan2',
        'title': 'blog post 2',
        'content': 'second',
        'date_posted': '???'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)