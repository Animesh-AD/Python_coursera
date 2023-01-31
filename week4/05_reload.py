import importlib
import sample
import sys
sys.path.insert(1, r'F:\New folder')
import filechange
def direct():
    try:
        # importlib.reload(filechange)   # reload function is funtion of importlib module it will print 
        print(filechange.files())
    except:
        pass
for i in range(5):
    direct()
    input('Hit enter to reload ')