import codecs



def tRXt_remove(hexarray: str, signature: str):

    position = hexarray.find(signature)
    i=0
    while position != -1:

        length_pos = position-8
        length_str = hexarray[length_pos:position]
        length = int(length_str, 16)
        chunk_length = (length+12)*2
        tmparray1 = hexarray[0:length_pos]
        tmparray2 = hexarray[length_pos+chunk_length]
        hexarray = tmparray1+tmparray2
        i = i + 1
        position = hexarray.find(signature)
    print("deleted " + str(i) + " chunks with signature:" + signature)