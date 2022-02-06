import time
import json
import os


def log(msg):
    ''' Prints @msg to the terminal with a timestamp '''
    localTime = time.localtime(time.time())
    stringTime = str(localTime[3]) + ":" + str(localTime[4]) + ":" + str(localTime[5])

    print stringTime + ": " + msg


def decodeJSON(data):
    '''Decodes JSON from a @data'''
    return json.loads(data)

def countFiles(folder):
    """ Counts the number of files in a directory """
    return sum(
        bool(os.path.isfile(os.path.join(folder, f)))
        for f in os.listdir(folder)
    )
