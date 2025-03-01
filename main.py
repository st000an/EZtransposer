import librosa
import librosa.display
import soundfile as sf
import numpy as np
from pydub import AudioSegment

AudioSegment.converter = r"D:\0-git\EZtransposer\ffmpeg-2025-02-26-git-99e2af4e78-full_build\ffmpeg-2025-02-26-git-99e2af4e78-full_build\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"D:\0-git\EZtransposer\ffmpeg-2025-02-26-git-99e2af4e78-full_build\ffmpeg-2025-02-26-git-99e2af4e78-full_build\bin\ffprobe.exe"

import os

def change_pitch(input_file, n_semitones, output_file="output.wav"):
    """

    :param input_file: str, 輸入音檔路徑 (支援 .wav 和 .mp3)
    :param n_semitones: int, 轉調的半音數 (正數為升調，負數為降調)
    :param output_file: str, 輸出 .wav 檔案名稱
    """
    temp_wav = None
    if input_file.lower().endswith('.mp3'):
        audio = AudioSegment.from_mp3(input_file)
        temp_wav = "temp_conversion.wav"
        audio.export(temp_wav, format="wav")
        input_file = temp_wav

    y, sr = librosa.load(input_file, sr=None)  

    # 轉調
    y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=n_semitones)

    sf.write(output_file, y_shifted, sr)
    if temp_wav and os.path.exists(temp_wav):
        os.remove(temp_wav)

    print(f"轉調完成，輸出檔案: {output_file}")

inputAudio=input(r"輸入檔案路徑(EX:D:\0-git\EZtransposer\韋禮安 Weibird Wei - 狼 Wolves (官方歌詞版).mp3)")
shiftNum=int(input("輸入轉調的半音數 (正數為升調，負數為降調)"))

#inputAudio=r"D:\0-git\EZtransposer\韋禮安 Weibird Wei - 狼 Wolves (官方歌詞版).mp3"
change_pitch(inputAudio, 3, inputAudio+"_output.wav") 

