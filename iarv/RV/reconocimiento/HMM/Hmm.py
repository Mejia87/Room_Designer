from hmmlearn import hmm
import numpy as np


class HMMdict:

    def __init__(self):
        self.__modelos_hmm = {"accion": {}, "direccion": {}, "numero": {}, "objetosuperior": {}, "objetoinferior": {}}

    def entrenar_hmm(self, mfccs, etiqueta, tipo, n_components=3, n_iter=100):
        modelo_hmm = hmm.GaussianHMM(n_components=n_components, covariance_type='diag', n_iter=n_iter)
        modelo_hmm.fit(mfccs)
        self.__modelos_hmm[tipo][etiqueta] = modelo_hmm

    def reconocer_palabra(self, mfccs, tipo_rec):
        puntajes = {}
        tipo_e = {}
        for tipo in tipo_rec:
            diccionario_tipo = self.__modelos_hmm[tipo]
            for etiqueta, modelo in diccionario_tipo.items():
                scor = modelo.score(mfccs)
                tipo_e[etiqueta] = tipo
                puntajes[etiqueta] = scor
        etiqueta_reconocida = max(puntajes, key=puntajes.get)
        return etiqueta_reconocida, tipo_e[etiqueta_reconocida]


