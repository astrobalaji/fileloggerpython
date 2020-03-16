import lorem
from random import randint

for i in range(10):
    file_len = randint(0,1000)
    sentences = [lorem.sentence()+'\n' for l in range(file_len)]
    f = open('file_safe/test_dat_{0}.dat'.format(i+1), 'w')
    f.writelines(sentences)
    f.close()
