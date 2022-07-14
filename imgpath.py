import random
import time


if __name__ == '__main__':
    while True:
        
        #print("yes")
        #time.sleep(1.0)

        commfile = open("image-service.txt", "r")
        path = commfile.readline()
        commfile.close()
        while not path or len(path) >2:
            time.sleep(1.0)
            commfile = open("image-service.txt", "r")
            path = commfile.readline()
            commfile.close()

        if len(path) <3: 
            print ("Passing image path...")
            num = int(path)%3
            print(num)
            commfile = open("image-service.txt", "w")
            commfile.write("images/"+ repr(num) +".jpg")
            commfile.close()
            time.sleep(1.0)