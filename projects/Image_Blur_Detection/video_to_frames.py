import cv2
import os

def get_video_file():
    while(True):
        try:
            #os.chdir("projects/Image_Blur_Detection")
            #print(os.listdir())
            path = input("Please enter folder location: ")
            relpath = "../"+path
            path = os.path.abspath(path)
            if(os.path.isfile(path)==True):
                break
            elif(os.path.isdir(relpath)):
                path = relpath
                break
            else:
                raise Exception

        except:
            print("Could not find path")
    return path

def get_frames_per_second():
    while(True):
        try:
            fps = float(input("Please enter the frames per second: "))
            if(fps <0 or fps>1000):
                raise Exception
            else:
                break
        except:
            print("Please enter a valid number")
    return fps

def get_frame(video,sec,count):
    video.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    boolean,image = video.read()
    if boolean:
        cv2.imwrite("image_holder/"+str(count)+".jpg",image)
    return boolean

def main():
    video_name = get_video_file()
    fps = get_frames_per_second()
    try:
        video = cv2.VideoCapture(video_name)
        sec = 0
        count = 1
        boolean = get_frame(video,sec,count)
        while(boolean):
            count += 1
            sec += fps
            sec = round(sec,2)
            boolean = get_frame(video,sec,count)

    except:
        print("Welp you tried")

        



main()