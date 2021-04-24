from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import argparse



parser = argparse.ArgumentParser(description = 'Envio de un mensaje a correos listados en un txt')
parser.add_argument('-l', help='Nombre de la lista con extension txt que contiene los correos a los cuales mandar el mensaje')
parser.add_argument('-e', help= 'Encabezado del mensaje a enviar')
parser.add_argument('-m', help='Mensaje a enviar a los correos de la lista')
args = parser.parse_args()

correo_remitente = str(args.l)
head = str(args.e)
message = str(args.m)
#FIN MODIFICACION



data = {}
with open('pass.json') as f:
	data = json.load(f)

msg = MIMEMultipart()




msg['From'] = data['user']

msg['To'] = correo_remitente
msg['Subject'] = head


msg.attach(MIMEText(message, 'plain'))


server = smtplib.SMTP('smtp.office365.com:587')

server.starttls()


print(data['user'])
server.login(data['user'], data['pass'])


server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("successfully sent email to %s:" % (msg['To']))
