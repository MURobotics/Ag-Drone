import cv2
import glob
import sys
import os

def get_folder():
    while(True):
        try:
            #os.chdir("projects/Image_Blur_Detection")
            #print(os.listdir())
            path = input("Please enter folder location: ")
            relpath = "../"+path
            path = os.path.abspath(path)

            if(os.path.isdir(path)==True):
                break
            elif(os.path.isdir(relpath)):
                path = relpath
                break
            else:
                raise Exception

        except:
            print("Could not find path")
    return path

def get_threshold():
    while(True):
        try:
            threshold = float(input("Please enter the treshold (0-100): "))
            if(threshold <0 or threshold>100):
                raise Exception
            else:
                break
        except:
            print("please enter a number between 0 and 100")
    return threshold
        
def get_images(path):
    image_list = []
    name_list = []
    try:
        print(path)
        for image in glob.glob(path+'/'+"*.jpg"):
            holder = cv2.imread(image)
            image_list.append(holder)
            name_list.append(image[len(path)+1:])
    except:
        print("Could not create image list")
    return image_list, name_list

def get_clear_images(image_list, treshold, name_list):
    clear_list = []
    clear_name_list = []
    i = 0
    try:
        for image in image_list:
            gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = cv2.Laplacian(gray_scale, cv2.CV_64F).var()
            print("Run " + str(i) + ": "+str(fm))

            if(fm > treshold):
                clear_list.append(image)
                clear_name_list.append(name_list[i])
            i += 1
    except:
        print("Could not create clear image list")

    return clear_list, name_list

def create_clear_folder(image_list, path, name_list):
    new_path = path+"_new"
    try:
        if(os.path.isdir(new_path)==False):
            os.mkdir(new_path)
    except:
        print("Could not make new directory")
    try:
        i=0
        for image in image_list:
            cv2.imwrite(new_path+"/"+name_list[i], image)
            
            i+=1
    except:
        print("Could not save images, call a priest if you got this far")

def main():
    path = get_folder()
    treshold = get_threshold()
    image_list, name_list= get_images(path)
    clear_list, clear_name_list = get_clear_images(image_list,treshold, name_list)
    create_clear_folder(clear_list,path, clear_name_list)


if __name__ =="__main__":
    main()