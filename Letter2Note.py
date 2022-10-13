from email.mime import base
import winsound
import random
from midiutil.MidiFile import MIDIFile

# notes range from A=440 Hz (C range)
frequency1 = 262 # Set Frequency To 262 Hertz (C)
frequency1b = 277 # C#/Db
frequency2 = 294 # D
frequency2b = 311 # D#/Eb
frequency3 = 330 # E
frequency4 = 349 # F
frequency4b = 370 # F#/Gb
frequency5 = 392 # G
frequency5b = 415 # G#/Ab
frequency6 = 440 # A
frequency6b = 466 # A#/Bb
frequency7 = 494 # B
frequency8 = 523 # C
frequency8b = 554 # C#/Cb
frequency9 = 587 # D
frequency9b = 622 # D#/Db
frequency10 = 659 # E
frequency10b = 698 # F
frequency11 = 740 # F#/Gb
frequency12 = 784 # G
frequency12b = 830 # G#/Ab
frequency13 = 880 # A
frequency13b = 932 # A#/Bb
frequency14 = 989 # B
frequency15 = 1046 # C

midi_song = MIDIFile(1)
track = 0
time = 0
tempo = 100 # In BPM
midi_song.addTempo(track, time, tempo)
#degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number # C major

# for i, pitch in enumerate(degrees):
#     midi_song.addNote(track, 0, pitch, time + i, 1, 100)

# tempo where duration = 1000 ms == 1 second
crotchet = 1000 # duration of a crochet (1 second)
minim = 1000*2 # duration of a minim (2 seconds)
quaver = 1000/2 # duration of a quaver (1/2 second)
semibreve = 1000*4 # duration of a semibreve (4 seconds)

# # Test
# winsound.Beep(frequency1, duration)
# winsound.Beep(frequency2, duration)
# winsound.Beep(frequency3, duration)
# winsound.Beep(frequency4, duration)
# winsound.Beep(frequency5, duration)
# winsound.Beep(frequency6, duration)
# winsound.Beep(frequency7, duration)
# winsound.Beep(frequency8, duration)

base_duration = 1#1000/2 (beats)
duration_dict = {
    "crotchet" : base_duration, # duration of a crochet (1 second)
    "minim" : base_duration*2, # duration of a minim (2 seconds)
    "quaver" : base_duration/2, # duration of a quaver (1/2 second)
    "semibreve" : base_duration/4, # duration of a semibreve (4 seconds)
}

letter2frequency_tab = {
"a" : frequency1,
"b" : frequency1b,
"c" : frequency2,
"d" : frequency2b,
"e" : frequency3,
"f" : frequency4,
"g" : frequency4b,
"h" : frequency5,
"i" : frequency5b,
"j" : frequency6,
"k" : frequency6b,
"l" : frequency7,
"m" : frequency8,
"n" : frequency8,
"o" : frequency8b,
"p" : frequency9,
"q" : frequency9b,
"r" : frequency10,
"s" : frequency10b,
"t" : frequency11,
"u" : frequency12,
"v" : frequency12b,
"w" : frequency13,
"x" : frequency13b,
"y" : frequency14,
"z" : frequency15,
}

letter2duration = {}

song = str(input("Enter a poem : ")) #"Le son des oiseaux sur la plage en couleur"
harmony1 =  str(input("Enter a poem for harmony : "))

# associate radomly the letters in letter2frequency_tab with the ones from duration_dict
for letter in letter2frequency_tab.keys():
    letter2duration.update({letter : list(duration_dict.values())[random.randint(0, 3)]})

# Loop over the different letters in song and replace them by their respective frequency
# for letter in song.lower().replace(" ",""):
#     winsound.Beep(letter2frequency_tab[letter], int(letter2duration[letter]))

# midi_song.addTempo(track,int(len(song.lower().replace(" ", "")))/6,80)
# midi_song.addTempo(track,int(len(song.lower().replace(" ", "")))/5,100)
# midi_song.addTempo(track,int(len(song.lower().replace(" ", "")))/4,120)
# midi_song.addTempo(track,int(len(song.lower().replace(" ", "")))/3,80)
# midi_song.addTempo(track,int(len(song.lower().replace(" ", "")))/2,100)

#int(len(song.lower().replace(" ", ""))/2)

# Tempo pattern
letter2tempo_tab = {}

for tem in letter2frequency_tab.keys():
    letter2tempo_tab.update({tem : list(duration_dict.values())[random.randint(0, 3)]})

print(letter2tempo_tab)

# change the time at which the note is written on the sheet music

#midi_song.addTempo(track, len(song.lower().replace(" ", "")), 80)

#rythm_pattern = [base_duration, base_duration/2, base_duration/2, base_duration/4, base_duration/4, base_duration/4, base_duration/4, base_duration, base_duration*2]
#rythm_pattern1 = [1, 1, 0.5, 0.25, 0.25, 0.25, 0.25, 2]
#rythm_pattern2 = [1, 0.5, 0.5, 1, 1, 0.5, 0.5, 2]

# Loop over the different letters in harmony1 and replace them by their respective frequency
for i, letter in enumerate(song.lower().replace(" ", "")):
    #note_duration = rythm_pattern[i%len(rythm_pattern)]
    #midi_song.addNote(track, 0, ord(letter)-50, time+i, note_duration, 100)
    #midi_song.addNote(track, 0, ord(letter)-53, time+i, note_duration, 100)
    #midi_song.addNote(track, 0, ord(letter)-55, time+i, note_duration, 100)
    #midi_song.addNote(track, 0, ord(letter)-57, time+i, note_duration, 100)
    midi_song.addNote(track, 0, ord(letter)-50, time, letter2tempo_tab[letter], 100)
    midi_song.addText(track, time, letter)
    time = time + letter2tempo_tab[letter]

with open("major-scale.mid", "wb") as output_file:
    midi_song.writeFile(output_file)









