from pydub import AudioSegment
sound = AudioSegment.from_wav('ifile.wav') 
sound.export('ofile.mp3', format='mp3')
