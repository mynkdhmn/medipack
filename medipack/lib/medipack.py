import os
import subprocess as sp

from lib.srbColour import Colour

class Medipack:
    def getLength(filename):
        result = sp.Popen(["ffprobe", filename],
            stdout = sp.PIPE, stderr = sp.STDOUT)
        arr = [x for x in result.stdout.readlines() if "Duration".encode('utf-8') in x]
        x = arr[0].decode('utf-8')
        x = x.split(' ')
        dur = x.index('Duration:') + 1
        return x[dur].split('.')[0]


    def video_trimmer(inp,trimmer,out):
        video_codec = " -c:v copy "
        audio_codec =  " -c:a copy "
        exec_command = 'ffmpeg -i ' + str(inp) + trimmer + video_codec + audio_codec + out
        Colour.print(exec_command,Colour.GREEN)
        os.system(exec_command)

    def video_cropper(inp,trimmer,out):
        video_codec = "" # senseless to say 'crop video and copy video, both at same time'
        audio_codec =  " -c:a copy "
        exec_command = 'ffmpeg -i ' + str(inp) + filters + video_codec + audio_codec + out
        Colour.print(exec_command,Colour.GREEN)
        os.system(exec_command)

    def video_resizer(inp,resizer,out):
        video_codec = "" # senseless to say 'change quality video and copy video, both at same time'
        audio_codec =  " -c:a copy "
        exec_command = 'ffmpeg -i ' + str(inp) + resizer + video_codec + audio_codec + out
        Colour.print(exec_command,Colour.GREEN)
        os.system(exec_command)

    def audio_cutter(inp,trimmer,out):
        exec_command = 'ffmpeg -i ' + str(inp) + trimmer + codec + out
        Colour.print(exec_command,Colour.GREEN)
        os.system(exec_command)

