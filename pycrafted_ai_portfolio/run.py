from flask import Flask, render_template

app = Flask(__name__, template_folder='app/templates')  # Points to templates folder inside 'app'

@app.route('/')
def index():
    return render_template('index.html')  # This loads app/templates/index.html

if __name__ == '__main__':
    app.run(debug=True)
