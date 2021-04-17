import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def Text_To_Speech(text, filename):
    text_from_excel = str(text)
    language = 'hi'
    obj1 = gTTS(text=text_from_excel, lang=language, slow=False)
    obj1.save(filename)
    
# This function returns pydubs audio segment


def Merge_Audios(audios):
    Audios_Combined = AudioSegment.empty()
    for audio in audios:
        Audios_Combined += AudioSegment.from_mp3(audio)
    return Audios_Combined

def Generate_Skeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 - Generate "kripya dheyan dijiye"
    start = 88000
    finish = 90200
    Audio_Processed = audio[start:finish]
    Audio_Processed.export("1_hindi.mp3", format="mp3")


    # 3 - Generate "se chalkar"
    start = 91000
    finish = 92200
    Audio_Processed = audio[start:finish]
    Audio_Processed.export("3_hindi.mp3", format="mp3")


    # 5 - Generate "ke raaste"
    start = 94000
    finish = 95000
    Audio_Processed = audio[start:finish]
    Audio_Processed.export("5_hindi.mp3", format="mp3")


    # 7 - Generate "ko jaane wali gaadi sakhya"
    start = 96000
    finish = 98900
    Audio_Processed = audio[start:finish]
    Audio_Processed.export("7_hindi.mp3", format="mp3")


    # 9 - Generate "kuch hi samay mei platform sankhya"
    start = 105500
    finish = 108200
    Audio_Processed = audio[start:finish]
    Audio_Processed.export("9_hindi.mp3", format="mp3")


    # 11 - Generate "par aa rahi hai"
    start = 109000
    finish = 112250
    Audio_Processed = audio[start:finish]
    Audio_Processed.export("11_hindi.mp3", format="mp3")

def Generate_Announcement(filename):
    Read_File = pd.read_excel(filename)
    print(Read_File)
    for index, item in Read_File.iterrows():
        # 2 - Generate from-city
        Text_To_Speech(item['from'], '2_hindi.mp3')

        # 4 - Generate via-city
        Text_To_Speech(item['via'], '4_hindi.mp3')

        # 6 - Generate to-city
        Text_To_Speech(item['to'], '6_hindi.mp3')

        # 8 - Generate train no and name
        Text_To_Speech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10 - Generate platform number
        Text_To_Speech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement = Merge_Audios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    Generate_Skeleton()
    print("Now Generating Announcement...")
    Generate_Announcement("announce_hindi.xlsx")
    

