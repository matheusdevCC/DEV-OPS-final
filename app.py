from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# -----------------------------
# CONFIGURAÇÕES DO JWT
# -----------------------------
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# -----------------------------
# CONFIGURAÇÃO DO SWAGGER
# -----------------------------
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API DevOps Final",
        "description": "Documentação automática gerada pelo Flasgger",
        "version": "1.0.0"
    }
}

swagger = Swagger(app, template=swagger_template)


# -----------------------------
# ROTAS DA API
# -----------------------------

@app.route('/')
def home():
    """
    Rota inicial da API
    ---
    responses:
      200:
        description: API online
    """
    return jsonify(message="API is running"), 200


@app.route('/items', methods=['GET'])
def get_items():
    """
    Retorna itens de exemplo
    ---
    responses:
      200:
        description: Lista de itens
        schema:
          type: object
          properties:
            items:
              type: array
              items:
                type: string
    """
    return jsonify(items=["item1", "item2", "item3"]), 200


@app.route('/login', methods=['POST'])
def login():
    """
    Realiza login e retorna token JWT
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
        description: Token JWT criado
      400:
        description: Payload inválido
    """
    data = request.get_json(silent=True)

    if data is not None and "username" not in data:
        return jsonify(error="Invalid payload"), 400

    token = create_access_token(identity="user")
    return jsonify(access_token=token), 200


# Tratamento para outros métodos inválidos
@app.route('/login', methods=['GET', 'PUT', 'DELETE'])
def login_invalid_method():
    return jsonify(error="Method not allowed"), 405


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    """
    Rota protegida com JWT
    ---
    responses:
      200:
        description: OK (token válido)
    """
    return jsonify(message="Protected route"), 200


# -----------------------------
# EXECUÇÃO LOCAL
# -----------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1313)
