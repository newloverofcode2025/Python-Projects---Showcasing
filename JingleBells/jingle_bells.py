import pygame
import numpy as np
import time

# Initialize pygame sound system
try:
    pygame.mixer.init()
except Exception as error:
    print(f"Failed to initialize pygame mixer: {error}")
    exit(1)

# Note frequencies in Hertz
FREQUENCIES = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25,
    'SILENCE': 0  # For rest notes
}

# Function to play a musical note
def sound_play(note, length):
    if note == 'SILENCE':
        time.sleep(length)  # Pause for rest notes
        return

    freq = FREQUENCIES[note]
    sample_rate = 44100  # Samples per second
    t = np.linspace(0, length, int(sample_rate * length), False)

    # Create sine wave for the note
    wave = np.sin(freq * t * 2 * np.pi)
    audio_data = np.int16(wave * 32767)

    # Ensure the array is 2-dimensional for stereo playback
    audio_data = np.column_stack((audio_data, audio_data))

    # Play the sound
    try:
        sound = pygame.sndarray.make_sound(audio_data)
        sound.play()
        time.sleep(length)  # Wait for the note to finish
        sound.stop()
    except Exception as error:
        print(f"Error playing sound: {error}")

# Jingle Bells melody
MELODY = [
    ('E4', 0.5), ('E4', 0.5), ('E4', 1),
    ('E4', 0.5), ('E4', 0.5), ('E4', 1),
    ('E4', 0.5), ('G4', 0.5), ('C4', 0.5), ('D4', 0.5),
    ('E4', 1),
    ('F4', 0.5), ('F4', 0.5), ('F4', 0.5), ('F4', 0.5),
    ('F4', 0.5), ('E4', 0.5), ('E4', 0.5), ('E4', 0.5),
    ('E4', 0.5), ('D4', 0.5), ('D4', 0.5), ('E4', 0.5),
    ('D4', 1), ('G4', 1),
    ('E4', 0.5), ('E4', 0.5), ('E4', 1),
    ('E4', 0.5), ('E4', 0.5), ('E4', 1),
    ('E4', 0.5), ('G4', 0.5), ('C4', 0.5), ('D4', 0.5),
    ('E4', 1),
    ('F4', 0.5), ('F4', 0.5), ('F4', 0.5), ('F4', 0.5),
    ('F4', 0.5), ('E4', 0.5), ('E4', 0.5), ('E4', 0.5),
    ('E4', 0.5), ('D4', 0.5), ('D4', 0.5), ('E4', 0.5),
    ('D4', 1), ('G4', 1),
    ('G4', 0.5), ('G4', 0.5), ('G4', 0.5), ('G4', 0.5),
    ('G4', 0.5), ('F4', 0.5), ('F4', 0.5), ('F4', 0.5),
    ('F4', 0.5), ('E4', 0.5), ('E4', 0.5), ('E4', 0.5),
    ('E4', 0.5), ('D4', 0.5), ('D4', 0.5), ('E4', 0.5),
    ('D4', 1), ('G4', 1)
]

# Play the melody
def play_jingle_bells():
    print("Playing Jingle Bells... 🎵")
    for note, duration in MELODY:
        sound_play(note, duration)

if __name__ == '__main__':
    play_jingle_bells()