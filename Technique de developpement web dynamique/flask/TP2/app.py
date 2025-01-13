from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue sur mon application Flask!'

@app.route('/about')
def about():
    return 'À propos de nous'

# Route avec paramètre string
@app.route('/user/<username>')
def user_profile(username):
    return f'Profil de {username}'

# Route avec paramètre entier
@app.route('/article/<int:article_id>')
def show_article(article_id):
    return f'Article numéro {article_id}'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Message reçu de {name}'
    return '''
        <form method="POST">
            <input type="text" name="name">
            <button type="submit">Envoyer</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)