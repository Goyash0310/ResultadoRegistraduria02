from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioResultado.findAll()
    """
    Asignacion estudiante y materia a inscripción
    """
    def create(self,infoResultado,id_mesa,id_candidato):
        nuevoResultado=Resultado(infoResultado)
        laMesa=Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa=laMesa
        nuevoResultado.candidato=elCandidato
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de Resultado (mesa y candidato)
    """
    def update(self,id,infoResultado,id_mesa,id_candidato):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.año=infoResultado["año"]
        elResultado.semestre = infoResultado["semestre"]
        elResultado.notaFinal=infoResultado["votos totales"]
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)
    def delete(self, id):
        return self.repositorioResultado.delete(id)

    "Obtener todos los candidatos inscritos en una mesa"
    def listarCandidatosInscritosEnMesa(self,id_candidato):
        return self.repositorioResultado.getListadoCandidatosInscritosEnMesa(id_candidato)

    "Obtener notas mas altas por curso"
    def notasMasAltasPorCurso(self):
        return self.repositorioResultado.getMayorNotaPorCurso()
    "Obtener promedio de notas en materia"
    def promedioNotasEnCandidato(self,id_candidato):
        return self.repositorioResultado.promedioNotasEnCandidato(id_candidato)