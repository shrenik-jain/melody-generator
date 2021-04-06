import numpy as np
from utils.get_data import Generator

class Piano:

    def fetch_piano_notes():
        '''
        Returns a Dictionary for all the keys' frequencies on the piano
        '''
        octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B', 'C1', 'D1', 'E1'] 
        base_frequency = 261.63 
        
        note_freqs = {octave[i]: base_frequency * pow(2,(i/12)) for i in range(len(octave))}        
        note_freqs[''] = 0.0 
        
        return note_freqs

    
    def fetch_song_data(sampling_rate, music_notes):
        note_freqs = Piano.fetch_piano_notes()
        song = [Generator.fetch_wave_data(sampling_rate, note_freqs[note]) for note in music_notes.split('-')]
        song = np.concatenate(song)
        return song.astype(np.int16)

    
    def fetch_chord_data(sampling_rate, chords):
        chords = chords.split('-')
        note_freqs = Piano.fetch_piano_notes()
        
        chord_data = []
        for chord in chords:
            data = sum([Generator.fetch_wave_data(sampling_rate, note_freqs[note]) for note in list(chord)])
            chord_data.append(data)
        
        chord_data = np.concatenate(chord_data, axis=0)   

        return chord_data.astype(np.int16)