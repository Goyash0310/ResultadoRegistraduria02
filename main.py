from flask import jsonify
from flask import Flask
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorResultado import ControladorResultado
miControladorMesa=ControladorMesa()
miControladorPartido=ControladorPartido()
miControladorCandidato=ControladorCandidato()
miControladorResultado=ControladorResultado()

###################################################################################

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

##########################################MESA#########################################

@app.route("/mesa",methods=['GET'])
def getMesa():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)

########################################PARTIDO###########################################

@app.route("/partido",methods=['GET'])
def getPartido():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partido/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

######################################CANDIDATO#############################################

@app.route("/materias",methods=['GET'])
def getMaterias():
    json=miControladorMateria.index()
    return jsonify(json)
@app.route("/materias/<string:id>",methods=['GET'])
def getMateria(id):
    json=miControladorMateria.show(id)
    return jsonify(json)
@app.route("/materias",methods=['POST'])
def crearMateria():
    data = request.get_json()
    json=miControladorMateria.create(data)
    return jsonify(json)
@app.route("/materias/<string:id>",methods=['PUT'])
def modificarMateria(id):
    data = request.get_json()
    json=miControladorMateria.update(id,data)
    return jsonify(json)
@app.route("/materias/<string:id>",methods=['DELETE'])
def eliminarMateria(id):
    json=miControladorMateria.delete(id)
    return jsonify(json)
@app.route("/materias/<string:id>/departamento/<string:id_departamento>",methods=['PUT'])
def asignarDepartamentoAMateria(id,id_departamento):
    json=miControladorMateria.asignarDepartamento(id,id_departamento)
    return jsonify(json)
#####################################INSCRIPCION##############################################
@app.route("/inscripciones",methods=['GET'])
def getInscripciones():
    json=miControladorInscripcion.index()
    return jsonify(json)
@app.route("/inscripciones/<string:id>",methods=['GET'])
def getInscripcion(id):
    json=miControladorInscripcion.show(id)
    return jsonify(json)
@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.create(data,id_estudiante,id_materia)
    return jsonify(json)
@app.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['PUT'])
def modificarInscripcion(id_inscripcion,id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.update(id_inscripcion,data,id_estudiante,id_materia)
    return jsonify(json)
@app.route("/inscripciones/<string:id_inscripcion>",methods=['DELETE'])
def eliminarInscripcion(id_inscripcion):
    json=miControladorInscripcion.delete(id_inscripcion)
    return jsonify(json)
@app.route("/inscripciones/materia/<string:id_materia>",methods=['GET'])
def inscritosEnMateria(id_materia):
    json=miControladorInscripcion.listarInscritosEnMateria(id_materia)
    return jsonify(json)
@app.route("/inscripciones/notas_mayores",methods=['GET'])
def getNotasMayores():
    json=miControladorInscripcion.notasMasAltasPorCurso()
    return jsonify(json)
@app.route("/inscripciones/promedio_notas/materia/<string:id_materia>",methods=['GET'])
def getPromedioNotasEnMateria(id_materia):
    json=miControladorInscripcion.promedioNotasEnMateria(id_materia)
    return jsonify(json)
###################################################################################

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
