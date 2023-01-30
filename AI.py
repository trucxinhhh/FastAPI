from pydub import AudioSegment
import math
import speech_recognition as sr
import os

# files                                                                         

r = sr.Recognizer()
class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename 
        self.audio = AudioSegment.from_wav(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 20 * 1000
        t2 = to_min * 20 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 20)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')
def MP3_TO_WAV(A,B):
    sound = AudioSegment.from_mp3(A)
    sound.export(B, format="wav")
def tong_hop(path):
        all_file = []
        all_text = []
        text = ""
        cau_hoi = ""
        dap_an = ""
        tra_loi = ""
        list = []
        list_1 = []
        list_2 = []
        list_3 = []
        # Change the directory
        os.chdir(path)
        # iterate through all file
        for file in os.listdir():
            # Check whether file is in text format or not
            if file.endswith(".wav"):
                file_path = f"{path}\{file}"
                # call read text file function
                all_file.append(file_path)
        del all_file[-1]

        for file in all_file:
        # open the file
            with sr.AudioFile(file) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text)
                text_1 = r.recognize_google(audio_data,language="vi")
                all_text.append(text_1)
        print(all_text)
        for item in all_text:
            text += ' ' + item   
        list = text.split()
        print(list)
    

folder = "D:\Science project\AI\Speech to Text with Python\Audio_wav\Ba_cau_hoi"
file = "Ba_cau.wav"
split_wav = SplitWavAudioMubin(folder, file)
split_wav.multiple_split(min_per_split=1)
tong_hop(folder)

