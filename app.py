from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flasgger import Swagger


app = Flask(__name__)

# JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)


# Swagger
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API DevOps Final",
        "description": "Documentação automática gerada pelo Flasgger",
        "version": "1.0.0"
    }
}

swagger = Swagger(app, template=swagger_template)


@app.route('/')
def home():
    return jsonify(message="API is running"), 200


@app.route('/items', methods=['GET'])
def get_items():
    """
    Lista de itens
    ---
    responses:
      200:
        description: Lista de itens
    """
    return jsonify(items=["item1", "item2", "item3"]), 200


@app.route('/login', methods=['POST'])
def login():
    """
    Gera token JWT
    ---
    parameters:
      - name: body
        in: body
        required: false
        schema:
          type: object
          properties:
            username:
              type: string
    responses:
      200:
        description: Token criado
    """
    data = request.get_json(silent=True)

    if data is not None and "username" not in data:
        return jsonify(error="Invalid payload"), 400

    token = create_access_token(identity="user")
    return jsonify(access_token=token), 200


@app.route('/login', methods=['GET', 'PUT', 'DELETE'])
def login_invalid_method():
    return jsonify(error="Method not allowed"), 405


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    Rota protegida
    ---
    responses:
      200:
        description: OK
    """
    return jsonify(message="Protected route"), 200
