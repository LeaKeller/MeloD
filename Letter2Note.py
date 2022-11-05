import random
from midiutil.MidiFile import MIDIFile

midi_song = MIDIFile(1)
track = 0
time = 0
tempo = 100 # In BPM
midi_song.addTempo(track, time, tempo)

base_duration = 1 # (beats)
duration_dict = {
    "crotchet" : base_duration, # duration of a crochet (1 second)
    "minim" : base_duration*2, # duration of a minim (2 seconds)
    "quaver" : base_duration/2, # duration of a quaver (1/2 second)
    "semibreve" : base_duration/4, # duration of a semibreve (4 seconds)
}

alphabet = [
"a",
"b",
"c",
"d",
"e",
"f",
"g",
"h",
"i",
"j",
"k",
"l",
"m",
"n",
"o",
"p",
"q",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z"
]

letter2duration = {}

song = str(input("Enter a poem : ")) # "The poetry of the new"

# associate radomly the letters in letter2frequency_tab with the ones from duration_dict
random.seed(8)

for letter in alphabet:
    letter2duration.update({letter : list(duration_dict.values())[random.randint(0, 3)]})

# Tempo pattern
letter2tempo_tab = {}

for tem in alphabet:
    letter2tempo_tab.update({tem : list(duration_dict.values())[random.randint(0, 3)]})

# Note scale
def make_scale(notes):
    keys = ['C', 'D♭', 'D', 'E♭', 'E', 'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B']

    scale = []

    for i in range(128):
        if keys[i%12] in notes:
            scale.append(i)
    return scale

C_major = make_scale(['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'])
D_major = make_scale(['D', 'E', 'G♭', 'G', 'A', 'B', 'D♭'])

# Loop over the different letters in harmony1 and replace them by their respective frequency
for i, letter in enumerate(song.lower().replace(" ", "")):
    midi_song.addNote(track, 0, D_major[ord(letter)-75], time, letter2tempo_tab[letter], 100)
    time = time + letter2tempo_tab[letter]
    midi_song.addText(track, 0, song)

with open("song.mid", "wb") as output_file:
    midi_song.writeFile(output_file)