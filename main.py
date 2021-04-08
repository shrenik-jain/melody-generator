from utils.get_data import Generator
from utils.virtual_piano import Piano
from scipy.io.wavfile import write
import numpy as np

if __name__ == '__main__':

    sampling_rate = 50000
    # twinkle-twinkle
    # music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C'

    # jingle-bells
    # music_notes = 'D-B-A-G-D-D-D-D-B-A-G-E--E-C1-B-A-f-D1-D1-C1-A-B--D-B-A-G-D--D-B-A-G-E--E-E-C1-B-A-D1-D1-D1-D1-E1-D1-C1-A-G--D1--B-B-B--B-B-B--B-D1-G-A-B--C1-C1-C1-C1-C1-B-B-B-B-B-A-A-B-A--D1--B-B-B--B-B-B--B-D1-G-A-B--C1-C1-C1-C1-C1-B-B-B-B-D1-D1-C1-G'
    
    # SaReGaMa
    # music_notes = 'C-D-E-F-G-A-B-C1-C1-B-A-G-F-E-D-C'
    
    # happy-birthday
    music_notes = 'C-C-D-C-F-E--C-C-D-C-G-F--C-C-C1-A-G-E-D--a-a-A-F-G-F'

    piano = Piano()
    generate = Generator()

    data = Piano.fetch_song_data(sampling_rate, music_notes)
    data = data * (16300 / np.max(data))

    Generator.waveform(sampling_rate)

    # write('tunes/twinkle-twinkle.wav', sampling_rate, data.astype(np.int16))
    # write('tunes/jingle-bells.wav', sampling_rate, data.astype(np.int16))
    # write('tunes/saregama.wav', sampling_rate, data.astype(np.int16))
    write('tunes/happy-birthday.wav', sampling_rate, data.astype(np.int16))

    chords = 'EgB-DfA-AcE-BDf-gAcE-fAc'
    data = Piano.fetch_chord_data(sampling_rate, chords)
    data = data * (16300/np.max(data))
    data = np.resize(data, (len(data)*5,))
    write('tunes/exp-C-Major.wav', sampling_rate, data.astype(np.int16))
