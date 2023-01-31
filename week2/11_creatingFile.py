'''try:
    with open('hitext.txt','w') as file: #creating file * also puted in try block to avoid exeption 
        file.writelines(['Hello i am crating new file','\nthis is another line']) # insering multiline using list 
except Exception as a:
    print(a, 'file is not present here')'''
try:
    with open('newtext.txt','w') as file:
        file.wr(['Hi my name is Animesh Das, this is new line i am writting'])
except FileNotFoundError as e:
    print('error', e)