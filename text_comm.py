import random
import time


if __name__ == '__main__':
    while True:

        commfile = open("textcomm.txt", "r")
        content = commfile.readline()
        commfile.close()
        while not content:
            time.sleep(1.0)
            commfile = open("textcomm.txt", "r")
            content = commfile.readline()
            commfile.close()

        if content: 
            print ("Calling graph generator...")
            #randnum = random.randint(0, 100)
            commfile = open("image-service.txt", "w")
            print(content[0])
            commfile.write(content[0])
            commfile.close()
            time.sleep(1.0)

            commfile = open("textcomm.txt", "w")
            commfile.write("")
            commfile.close()