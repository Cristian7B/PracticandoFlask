from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/api/showdata", methods=['GET'])
def api():
    respuesta = {
        "mensaje": "Hola, bienvenido a la API!",
        "estado": "exito"
    }
    return jsonify(respuesta)


usuarios = [
    {
        "nombre": "Cristian Camilo Bonilla Lizarazo",
        "codigo": "123123123",
        "correo": "ccbonillal@udistrital.edu.co"
    },
    {
        "nombre": "Juan David Bonilla Lizarazo",
        "codigo": "123123124",
        "correo": "jdbonillal@udistrital.edu.co"
    },
    {
        "nombre": "Laura Sofia Lizarazo",
        "codigo": "123123125",
        "correo": "lslizarazo@udistrital.edu.co"
    }
]

@app.route("/api/validar", methods=["POST"])
def api_validar():
    data_json = request.get_json()
    email = data_json.get("email")
    
    for usuario in usuarios:
        if usuario["correo"] == email:
            return jsonify({"mensaje": "Usuario encontrado", "usuario": usuario, "estado": "exito"}), 200
    
    return jsonify({"mensaje": "Usuario no encontrado", "estado": "error"}), 500



if __name__ == '__main__':
    app.run(debug=True)