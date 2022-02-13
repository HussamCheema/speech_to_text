# Converting mp3 to wav
from pydub import AudioSegment
import wave, array

def convert_to_wav(mp3_path, output_path):
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(output_path, format="wav")


# Converting wav to mp3
def convert_to_mp3(wav_path, output_path):
    sound = AudioSegment.from_wav(wav_path)
    sound.export(output_path, format="mp3")


# Convert stereo to mono
def convert_stereo_to_mono(signal):
    if signal.ndim == 2:
        if signal.shape[1] == 1:
            signal = signal.flatten()
        else:
            if signal.shape[1] == 2:
                signal = (signal[:, 1] / 2) + (signal[:, 0] / 2)
    return signal



# Convert mono to stereo
def convert_mono_to_stereo(file1, output):
    ifile = wave.open(file1)
    # print(ifile.getparams())
    # (1, 2, 44100, 2013900, 'NONE', 'not compressed')
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = ifile.getparams()
    # assert comptype == 'NONE'  # Compressed not supported yet
    
    array_type = {1:'B', 2: 'h', 4: 'l'}[sampwidth]
    left_channel = array.array(array_type, ifile.readframes(nframes))[::nchannels]
    ifile.close()

    stereo = 2 * left_channel
    stereo[0::2] = stereo[1::2] = left_channel

    ofile = wave.open(output, 'w')
    ofile.setparams((2, sampwidth, framerate, nframes, comptype, compname))
    ofile.writeframes(stereo.tostring())
    ofile.close()