import malaya_speech
import noisereduce as nr


# Spectral Gating Algorithm
def spectral_gating(signal, sample_rate):
    reduced_noise = nr.reduce_noise(y=signal, sr=sample_rate)
    return reduced_noise


# Malaya Speech Wave-U-Net
def wave_u_net(path, sample_rate, model="resnet-unet", quantized=True):
    malaya_speech.noise_reduction.available_model()
    quantized_model = malaya_speech.noise_reduction.deep_model(model=model, quantized=quantized)
    # file_path should contain wav file
    y, sr = malaya_speech.load(path, sr=sample_rate)
    output = quantized_model(y)

    # return slice of the output like this
    # return output['voice'][:20 * sr]

    return output


