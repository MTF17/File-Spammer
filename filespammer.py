import os


name = ("hello")# name of the files
text = ("nick is here")# text in the files 

a = 0
while True:

    a += 1
    with open((name)+ str(a), 'w') as f:
        f.write(message)

# it's sth very simple and anyone can make sth like this or better, try making it over again with a gui !! good luck ! 
