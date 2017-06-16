'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
def read_int(message):
    s = input(message)
    try:
        return int(s)
    except:
        raise Exception("Invalid integer.")