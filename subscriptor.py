import smtplib
from email.mime.text import MIMEText

def subscriptor(mensaje):
    # Configuración del correo electrónico
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    usuario_smtp = 'guest'
    clave_smtp = 'guest'
    destinatario = 'buenas@example.com'

    # Crear el mensaje de correo electrónico
    msg = MIMEText(mensaje)
    msg['Subject'] = 'Mensaje de la cola'
    msg['From'] = usuario_smtp
    msg['To'] = destinatario

    # Enviar el correo electrónico
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(usuario_smtp, clave_smtp)
    servidor.sendmail(usuario_smtp, destinatario, msg.as_string())
    servidor.quit()

    print('Correo electrónico enviado')
