import os, time

def robot(text):
    os.system("espeak ' " + text + " ' ")
robot('What is your name')
name = input('What is your name?: ')
robot("Nice to meet you " + name)
robot("What is the colour of the sky?")
sky = input("What is the colour of the sky?:")
if sky == "blue":
    robot("What is the opposite to ... down")
    down = input("What is the opposite of down?:")
    if down == "up":
        robot(name + sky + down)
        print(name + " " + sky + " " + down + " ")
                                            
    
      
