from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

### Swagger UI ###
SWAGGER_URL = '/swagger'
API_DOC_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOC_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/')
def home():
    return jsonify(message="API is running"), 200


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items=["item1", "item2", "item3"]), 200


@app.route('/login', methods=['POST'])
def login():

    # validação opcional de payload
    data = request.get_json(silent=True)

    if data is not None and "username" not in data:
        return jsonify(error="Invalid payload"), 400

    # token de acesso
    access_token = create_access_token(identity="user")
    return jsonify(access_token=access_token), 200


# Tratamento do método inválido (GET, PUT etc.)
@app.route('/login', methods=['GET', 'PUT', 'DELETE'])
def login_invalid_method():
    return jsonify(error="Method not allowed"), 405


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="Protected route"), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1313)
