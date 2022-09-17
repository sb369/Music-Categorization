import os

n = 30
path = os.getcwd()+'/test_audio'

def single_cutter(n, path):
    for filename in os.listdir(path):
        print(path)
        if (filename.endswith(".mp3")): #or .avi, .mpeg, whatever.
            print(filename)
            total_path = path+'/'+filename
            print(total_path)
            os.system("ffmpeg -i '{0}' -f segment -segment_time {1} -c copy '{2}'%03d.mp3".format(total_path, n, filename))
        else:
            continue


single_cutter(n, path)
