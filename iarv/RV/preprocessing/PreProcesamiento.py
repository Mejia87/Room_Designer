import librosa
import librosa.display
import numpy as np
import sounddevice as sd
import soundfile as sf
from scipy.signal import medfilt
from iarv.RV.Dir import REC_RAW, REC_PROC


def preprocesar_audio(audio_path, threshold, hop_length=512):
    audio, sr = librosa.load(audio_path)

    audio = librosa.to_mono(audio)

    audio_normalizado = librosa.util.normalize(audio)

    audio_resampled = librosa.resample(audio_normalizado, orig_sr=librosa.get_samplerate(audio_path), target_sr=16000)

    audio_filtrado = medfilt(audio_resampled, kernel_size=3)

    audio_filtrado = np.int16(audio_filtrado * 32767)
    tramos_activos = librosa.effects.split(audio_filtrado, top_db=threshold, hop_length=hop_length)

    audio_sin_espacios, _ = librosa.effects.trim(audio_filtrado)

    mfccs = []
    for inicio, fin in tramos_activos:
        audio_sin_espacios = []
        audio_sin_espacios.extend(audio_filtrado[inicio:fin])
        audio_sin_espacios = np.array(audio_sin_espacios)
        sf.write(audio_path, audio_sin_espacios, sr)
        data = extraer_mfcc(audio_path)
        mfccs.append(data)
    return mfccs


def extraer_mfcc(ruta_audio, n_mfcc=40):
    y, sr = librosa.load(ruta_audio)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    #mfccs_t = np.mean(mfccs.T, axis=0)
    return mfccs.T  # Transponer para tener frames x n_mfcc


def grabar_audio(duracion, nombre, sr=16000):
    print("#####...Grabando...####")
    audio = sd.rec(int(duracion * sr), samplerate=sr, channels=1)
    sd.wait()  # Espera a que la grabación termine
    print("Grabación completada.")
    sf.write(nombre, audio, sr)
    sf.write(REC_RAW, audio, sr)

