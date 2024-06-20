from iarv.RV.preprocessing.PreProcesamiento import grabar_audio, preprocesar_audio
from iarv.RV.reconocimiento.HMM.Hmm import HMMdict
import pandas as pd
from iarv.RV.Dir import CSV, REC_PROC
from iarv.RV.comandos import IteradorComando

def __entrenarModelo_dict(csv):
    df = pd.read_csv(csv)
    hmmc = HMMdict()
    print("entrenando...")
    for etiqueta in df['etiqueta'].unique():
        caracteristicas = df[df['etiqueta'] == etiqueta]
        tipo = caracteristicas['tipo'].unique()[0]
        carac_mfccs = caracteristicas.drop(columns=['etiqueta', 'tipo']).values
        hmmc.entrenar_hmm(carac_mfccs, etiqueta, tipo)
    print("entrenamiento finalizado.")
    return hmmc



def reconocer_voz(duracion=5, trhhold=28):
    modelo = __entrenarModelo_dict(CSV)

    #  Pre Procesamiento
    grabar_audio(duracion,  nombre=REC_PROC)
    mfccs_rec = preprocesar_audio(REC_PROC, threshold=trhhold)
    print("Reconociendo...")
    palabras = []
    tipo = ["accion"]
    iterador = IteradorComando()
    for mfccs in mfccs_rec:
        if not tipo is None:
            texto, nt = modelo.reconocer_palabra(mfccs, tipo)
            tipo = iterador.iterarComando(texto if tipo[0] == "accion" else nt)
            palabras.append(texto)
    return palabras
