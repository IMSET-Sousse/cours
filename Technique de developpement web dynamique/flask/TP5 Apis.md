# TP5: APIs avec Flask

## Objectifs d'apprentissage

- Comprendre les concepts fondamentaux des APIs REST
- Apprendre à créer des endpoints API avec Flask
- Maîtriser les méthodes HTTP (GET, POST, PUT, DELETE)
- Gérer la sérialisation et désérialisation JSON
- Implémenter l'authentification et la sécurité des APIs
- Documenter une API avec Swagger/OpenAPI

## Prérequis

- Avoir complété le TP3 sur les Templates
- Connaissances de base en HTTP et JSON
- Python et Flask installés
- Postman ou un outil similaire pour tester les APIs

## 1. Introduction aux APIs REST

Une API REST (Representational State Transfer) est un style d'architecture qui définit un ensemble de contraintes pour créer des services web.

### Principes REST

- Sans état (Stateless)
- Interface uniforme
- Système en couches
- Cache possible
- Resources identifiables

## 2. Configuration de Base

```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permet les requêtes cross-origin

# Base de données simulée
todos = [
    {"id": 1, "title": "Apprendre Flask", "completed": False},
    {"id": 2, "title": "Créer une API", "completed": False}
]

# Route de base
@app.route('/api/status')
def status():
    return jsonify({"status": "API is running"})
```

## 3. Création des Endpoints CRUD

### Lecture (GET)

```python
# Obtenir tous les todos
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Obtenir un todo spécifique
@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo)
```

### Création (POST)

```python
@app.route('/api/todos', methods=['POST'])
def create_todo():
    if not request.json or 'title' not in request.json:
        return jsonify({"error": "Title is required"}), 400
    
    todo = {
        "id": max(todo["id"] for todo in todos) + 1,
        "title": request.json["title"],
        "completed": request.json.get("completed", False)
    }
    todos.append(todo)
    return jsonify(todo), 201
```

### Mise à jour (PUT)

```python
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    
    todo["title"] = request.json.get("title", todo["title"])
    todo["completed"] = request.json.get("completed", todo["completed"])
    return jsonify(todo)
```

### Suppression (DELETE)

```python
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    initial_length = len(todos)
    todos = [todo for todo in todos if todo["id"] != todo_id]
    
    if len(todos) == initial_length:
        return jsonify({"error": "Todo not found"}), 404
    return '', 204
```

## 4. Gestion des Erreurs

```python
from werkzeug.exceptions import HTTPException

@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }), e.code

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400
```

## 5. Authentification avec JWT

```python
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app.config['JWT_SECRET_KEY'] = 'votre-secret-key'  # À changer en production
jwt = JWTManager(app)

# Route d'authentification
@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    # Vérification simplifiée (à adapter selon vos besoins)
    if username == "admin" and password == "password":
        access_token = create_access_token(identity=username)
        return jsonify({"token": access_token})
    
    return jsonify({"error": "Bad username or password"}), 401

# Route protégée
@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"message": "This is a protected endpoint"})
```

## 6. Documentation avec Swagger

```python
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Todo API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
```

## 7. Exercices Pratiques

1. **API de Base**
   - Créez une API CRUD pour gérer une liste de produits
   - Implémentez la validation des données
   - Gérez les erreurs appropriées

2. **Authentification**
   - Ajoutez l'authentification JWT
   - Créez des routes protégées
   - Implémentez différents rôles utilisateur

3. **Documentation**
   - Documentez votre API avec Swagger
   - Ajoutez des descriptions détaillées
   - Incluez des exemples de requêtes

## 8. Tests d'API

### Avec Postman

```
GET http://localhost:5000/api/todos
Authorization: Bearer <votre-token>

POST http://localhost:5000/api/todos
Content-Type: application/json
{
    "title": "Nouveau todo",
    "completed": false
}
```

### Avec Python et requests

```python
import requests

# Test GET
response = requests.get('http://localhost:5000/api/todos')
print(response.json())

# Test POST
data = {"title": "Nouveau todo", "completed": False}
response = requests.post('http://localhost:5000/api/todos', json=data)
print(response.json())
```

## 9. Bonnes Pratiques

1. **Sécurité**
   - Utilisez HTTPS en production
   - Implémentez une authentification robuste
   - Validez toutes les entrées utilisateur

2. **Performance**
   - Utilisez la mise en cache
   - Paginez les résultats
   - Optimisez les requêtes

3. **Documentation**
   - Documentez tous les endpoints
   - Incluez des exemples
   - Maintenez la documentation à jour

## Ressources Utiles

- [Documentation Flask-RESTful](https://flask-restful.readthedocs.io/)
- [Documentation Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [Documentation Swagger/OpenAPI](https://swagger.io/docs/)

## Dépannage Courant

1. **Problèmes CORS**
   - Vérifiez la configuration CORS
   - Assurez-vous que les en-têtes sont corrects
   - Testez avec différents clients

2. **Erreurs d'Authentification**
   - Vérifiez le token JWT
   - Assurez-vous que les credentials sont corrects
   - Vérifiez les en-têtes d'autorisation