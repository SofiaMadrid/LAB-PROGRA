#!/usr/bin/env python3
import hashlib 
import base64
from typing import Callable

def encode_decode_bytes(byte_message: bytes, encode_fn: Callable[[bytes], bytes]) -> bytes:
    return encode_fn(byte_message)


def encode_text(text: str, encoding_format: str = 'ascii') -> str:
    return encode_decode_bytes(text.encode(encoding_format), base64.b64encode).decode(encoding_format)


def decode_text(text: str, encoding_format: str = 'ascii') -> str:
    return encode_decode_bytes(text.encode(encoding_format), base64.b64decode).decode(encoding_format)


def encode_file(path:str) -> bytes:
    with open(path, 'rb') as file_to_encode:
        return encode_decode_bytes(file_to_encode.read(), base64.b64encode)


def decode_file(path:str) -> bytes:
    file_to_encode = open(path, 'rb')
    return encode_decode_bytes(file_to_encode.read(), base64.b64decode)


def save_file(path: str,content: bytes) -> None:
    with open(path, 'wb') as file_to_save:
        file_to_save.write(content)

def encode_plus_one(word:str) -> str:
    return "".join([chr(ord(character)+2) for character in word])

if __name__ == '__main__':
    import sys

    cmds = {'encode': base64.b64encode, 'decode': base64.b64decode}
    if len(sys.argv) > 1:
        main_cmd = sys.argv[1]
        encode_format = sys.argv[2] if len(sys.argv) > 2 else 'ascii'
        code_function = cmds.get(main_cmd, cmds.get('encode'))
        print(encode_decode_bytes(sys.stdin.read(), code_function))

   #Codifica y guarda el msg.txt
    save_file('msg_codificado.txt', encode_file('msg.txt'))
   
    #Codifica y guarda fcfm.png a un .txt
    save_file('fcfm_codificado.txt', encode_file('fcfm.png'))
    
    #Decodifica y guarda la imagen misteriosa de txt a un png.
    save_file('mystery_img.png', decode_file('mystery_img.txt'))

    #Decodifica y guarda la imagen misteriosa 2 de txt a un png.
    save_file('mystery_img2.png', decode_file('mystery_img2.txt'))

    #Verfifica que las imagenes tengan el sha256 correcto
 
    filename = input("Ingrese el nombre del archivo con su extensión: ")
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    print(sha256_hash.hexdigest())


    
