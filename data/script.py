import os

path = './surgical/'
files = os.listdir(path)
name = 'sm'

for i, j in zip(files, range(1, len(files)+1)):
    if i[len(i)-4:len(i)] == 'jpeg':
        suffix = '.jpeg'
    else:
        suffix = (i[len(i)-4:len(i)])
    os.rename(path + i, path + name + str(j) + suffix)
