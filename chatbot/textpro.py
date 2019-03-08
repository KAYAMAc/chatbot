
def openfiles():
    f=open('subtitle.txt','rb')
    p1=open('questions.txt','w',encoding='utf-8')
    p2=open('answers.txt','w',encoding='utf-8')
    '''line=f.readline().decode('UTF-8')'''
    line=f.readline()
    while(line!=''):
        p1.write(line)
        line = f.readline().decode('UTF-8','ignore')
        p2.write(line)
        line = f.readline().decode('UTF-8','ignore')
    f.close()
    p1.close()
    p2.close()


if __name__ == '__main__':
   openfiles();

# -*- coding:utf-8 -*-



