import os
import shutil
import time 



split_length = 30 ######### DEFAULT 30SECS
path = os.getcwd()

dest = os.path.join(path,"../test_data/myelin_test_split/")

if os.path.isdir(dest) == True:
        shutil.rmtree(dest)


if os.path.isdir(dest) == False:
        os.makedirs(dest)

print(dest)

def single_cutter(split_length, path):
    global dest
    for filename in os.listdir(path):
        print(path)
        if (filename.endswith((".mp3"))): ##### SUPPORTED TYPES
            print(filename)
            total_path = path+'/'+filename
            filename = dest + filename
            print(total_path)
            os.system("ffmpeg -i '{0}' -f segment -segment_time {1} -c copy '{2}'_%03d.mp3".format(total_path, split_length, filename))
        elif (filename.endswith((".wav"))): ##### SUPPORTED TYPES
            print(filename)
            total_path = path+'/'+filename
            filename = dest + filename
            print(total_path)
            os.system("ffmpeg -i '{0}' -f segment -segment_time {1} -c copy '{2}'_%03d.wav".format(total_path, split_length, filename))
        elif (filename.endswith((".m4a"))): ##### SUPPORTED TYPES
            print(filename)
            total_path = path+'/'+filename
            filename = dest + filename
            print(total_path)
            os.system("ffmpeg -i '{0}' -f segment -segment_time {1} -c copy '{2}'_%03d.m4a".format(total_path, split_length, filename))
        
        else:
            continue

def full_cutter(split_length, path):
    for root, subdirectories, files in os.walk(path):
        for subdirectory in subdirectories:
            single_cutter(split_length, os.path.join(root, subdirectory))



start = time.time()
########################################## CUSTOM SPLIT LENGTH ############################
full_cutter(split_length, path)
end = time.time()

print("Time", end-start)
#ffmpeg -i tamil_family.mp3 -f segment -segment_time 30 -c copy test_song%03d.mp3


#ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.png