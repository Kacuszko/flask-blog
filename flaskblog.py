from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Mateusz Kacalinski',
        'title': 'Flask Blog',
        'content': 'First post content',
        'date_posted': 'March 02, 2020'
    },
    {
        'author': 'Jarek Cynk',
        'title': 'Second post',
        'content': 'Second post content',
        'date_posted': 'March 03, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='Blog')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)