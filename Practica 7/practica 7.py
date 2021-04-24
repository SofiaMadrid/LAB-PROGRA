from ftplib import FTP
import os.path
ftp = FTP('ftp.rediris.es')     
ftp.login()                 
ftp.cwd('debian')              
ftp.retrlines('LIST')

def save_file(con: FTP, remote_file_path:str, local_file_path:str):
    with open(local_file_path,'wb') as local_file:
        con.retrbinary(f'RETR {remote_file_path}', local_file.write)

def get_txt_file(con: FTP, file_path:str):
    listado = []
    con.retrlines(f'RETR {file_path}', listado.append)
    return listado



with open('archivos.txt', 'wb') as fp:
    ftp.retrbinary('RETR README', fp.write)
    ftp.retrbinary('RETR README.html', fp.write)
    ftp.retrbinary('RETR README.mirrors.html', fp.write)
    ftp.retrbinary('RETR README.mirrors.txt', fp.write)
ftp.quit()

