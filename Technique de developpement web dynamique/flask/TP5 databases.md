# TP5: Bases de Données avec Flask et PostgreSQL

## Objectifs d'apprentissage

- Comprendre l'intégration de PostgreSQL avec Flask
- Maîtriser Flask-SQLAlchemy pour la gestion des bases de données PostgreSQL
- Apprendre à utiliser pgAdmin pour la gestion de base de données
- Effectuer des opérations CRUD avec PostgreSQL
- Gérer les relations entre les tables
- Implémenter des migrations de base de données
- Utiliser les fonctionnalités spécifiques à PostgreSQL

## Prérequis

- Avoir complété le TP4 sur les APIs
- Connaissances de base en SQL
- Python et Flask installés
- PostgreSQL 15 ou plus récent installé et configuré
- pgAdmin 4 installé et configuré
- Un utilisateur PostgreSQL avec les droits d'administration

## 1. Configuration du Projet

### Installation des Dépendances Python

```bash
pip install psycopg2-binary
pip install flask-sqlalchemy
pip install flask-migrate
```

### Configuration de Flask avec PostgreSQL

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Format: postgresql://username:password@host:port/database_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:votre_mot_de_passe@localhost:5432/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```

## 2. Création de la Base de Données

### Via pgAdmin

1. Ouvrir pgAdmin 4
2. Se connecter au serveur PostgreSQL
3. Clic droit sur "Databases"
4. Create > Database:
   - Database: flask_app
   - Owner: postgres

### Via SQL Shell (psql)

```sql
CREATE DATABASE flask_app;
CREATE USER flask_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE flask_app TO flask_user;
```

## 3. Modèles avec Types PostgreSQL

```python
from sqlalchemy.dialects.postgresql import JSON, ARRAY, UUID
import uuid

class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    preferences = db.Column(JSON)  # Stockage JSON pour les préférences
    tags = db.Column(ARRAY(db.String))  # Array PostgreSQL
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.Enum('draft', 'published', 'archived', name='post_status'))

    def __repr__(self):
        return f'<Post {self.title}>'
```

## 4. Migrations avec Alembic

```python
from flask_migrate import Migrate

migrate = Migrate(app, db)

# Dans le terminal:
# flask db init
# flask db migrate -m "Initial migration"
# flask db upgrade
```

### Vérification des Migrations dans pgAdmin

1. Ouvrir pgAdmin
2. Naviguer vers votre base de données
3. Schemas > Public > Tables
4. Vérifier la table 'alembic_version'

## 5. Opérations CRUD avec PostgreSQL

### Création avec Gestion des Transactions

```python
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        username=data['username'],
        email=data['email'],
        preferences=data.get('preferences', {}),
        tags=data.get('tags', [])
    )
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully', 'id': str(new_user.id)}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
```

### Requêtes Avancées PostgreSQL

```python
# Recherche Full-Text
from sqlalchemy import text

@app.route('/posts/search', methods=['GET'])
def search_posts():
    query = request.args.get('q', '')
    sql = text("""
        SELECT id, title, content
        FROM post
        WHERE to_tsvector('french', content) @@ plainto_tsquery('french', :query)
    """)
    result = db.session.execute(sql, {'query': query})
    return jsonify([dict(row) for row in result])

# Agrégations JSON
@app.route('/users/preferences/summary', methods=['GET'])
def preferences_summary():
    sql = text("""
        SELECT jsonb_object_agg(key, count(*))
        FROM user_table,
        jsonb_each(preferences) AS prefs(key, value)
        GROUP BY key
    """)
    result = db.session.execute(sql)
    return jsonify(dict(result.fetchone()))
```

## 6. Fonctionnalités Spécifiques PostgreSQL

### Index Avancés

```python
from sqlalchemy import Index

# Index GiST pour la recherche full-text
Index('idx_post_content_fts', text("to_tsvector('french', content)"), postgresql_using='gist')

# Index GIN pour les champs JSON
Index('idx_user_preferences', User.preferences, postgresql_using='gin')
```

### Triggers et Fonctions

```sql
-- Dans pgAdmin ou psql
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.modified_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_post_modtime
    BEFORE UPDATE ON post
    FOR EACH ROW
    EXECUTE FUNCTION update_modified_column();
```

## 7. Exercices Pratiques

1. **Système de Blog avec PostgreSQL**
   - Créez les modèles avec types PostgreSQL spécifiques
   - Implémentez la recherche full-text
   - Utilisez les fonctionnalités JSON pour les métadonnées

2. **Gestion des Médias**
   - Stockez les métadonnées des fichiers en JSON
   - Utilisez ARRAY pour les tags
   - Implémentez des requêtes complexes

3. **Analyse de Données**
   - Utilisez les fonctions d'agrégation PostgreSQL
   - Créez des vues matérialisées
   - Implémentez des rapports avec des requêtes complexes

## 8. Monitoring et Optimisation

### Utilisation de pgAdmin

1. **Analyse des Requêtes**
   - Explain Analyze
   - Query Tool
   - Query History

2. **Maintenance**
   - Vacuum
   - Reindex
   - Table Statistics

### Optimisation des Performances

```python
# Configuration du pool de connexions
app.config['SQLALCHEMY_POOL_SIZE'] = 5
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 10
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30

# Exemple de requête optimisée
@app.route('/posts/popular', methods=['GET'])
def get_popular_posts():
    return db.session.query(Post)\
        .options(db.joinedload(Post.author))\
        .filter(Post.status == 'published')\
        .order_by(db.desc(Post.views))\
        .limit(10)\
        .all()
```

## 9. Tests avec Base de Test PostgreSQL

```python
import unittest
from app import app, db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/flask_test'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        user = User(
            username='test',
            email='test@test.com',
            preferences={'theme': 'dark'},
            tags=['python', 'flask']
        )
        db.session.add(user)
        db.session.commit()
        assert User.query.count() == 1
```

## Ressources Utiles

- [Documentation PostgreSQL](https://www.postgresql.org/docs/)
- [Documentation pgAdmin](https://www.pgadmin.org/docs/)
- [Documentation psycopg2](https://www.psycopg.org/docs/)
- [Documentation Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)

## Dépannage Courant

1. **Problèmes de Connexion**
   - Vérifiez les paramètres de connexion PostgreSQL
   - Assurez-vous que le service PostgreSQL est en cours d'exécution
   - Vérifiez les permissions de l'utilisateur

2. **Optimisation des Performances**
   - Utilisez EXPLAIN ANALYZE dans pgAdmin
   - Vérifiez les index manquants
   - Optimisez les requêtes complexes

3. **Gestion des Migrations**
   - Sauvegardez la base avant les migrations
   - Testez les migrations sur un environnement de test
   - Gardez un historique des migrations