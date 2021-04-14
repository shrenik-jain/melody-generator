import numpy as np  
import matplotlib.pyplot as plt

class Generator: 

    def fetch_wave_data(sampling_rate, frequency, duration=0.5):
        '''
        Takes frequency and duration for a wave as input and 
        returns an array of values at all points in time.
        '''
        amplitude = 4000
        time = np.linspace(0 , duration , int(sampling_rate * duration))
        wave = amplitude * np.sin(2 * np.pi * frequency * time)

        return wave

    
    def waveform(sampling_rate):
        a_wave = Generator.fetch_wave_data(sampling_rate, 500 , 1)
        plt.figure()
        plt.plot(a_wave[0 : int(sampling_rate / 500)])
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.show()

'''
The frequency of 500Hz implies that the wave completes 500 full cycles 
in one second. In other words, it completes one cycle in 1/500 second.
Since we divided our 1 second into 50000 parts, according to the sampling_rate, 
we can plot our one cycle by printing elements from 0 to 100 i.e. int(50000/500)
'''
