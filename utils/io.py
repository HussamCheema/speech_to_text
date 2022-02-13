from scipy.io import wavfile
import librosa
import soundfile as sf

# Read mp3 audio file
def read_mp3(path):
    signal, sr = librosa.load(path)
    return signal, sr


# Read wav audio file
def read_wav(wavfile, path):
    sample_rate, signal = wavfile.read(path)
    return sample_rate, signal


# Write mp3 audio file
def write_mp3(output_path, signal, sample_rate):
    sf.write(output_path, signal, sample_rate)


# Write wav audio file
def write_wav(wavfile, signal, sample_rate, path):
    wavfile.write(path, sample_rate, signal)


# Write mono channel to mp3 and wav
def write_mono_to_file():
    pass