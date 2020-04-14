import codecs

def tEXt_show(hexarray: str, signature: str):
    position = hexarray.find(signature)
    if position != -1:
        length_pos = position - 8
        length_str = hexarray[length_pos:position]
        length = int(length_str, 16)
        position_data = position + 8
        chunk_data = codecs.decode(hexarray[position_data:position_data+ length*2], "hex").decode('utf-8')
        print("tEXt Content:" + chunk_data)