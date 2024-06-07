import pika

# Conectar a RabbitMQ
conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

# Declarar la cola
canal.queue_declare(queue='cola_de_mensajes')

# Enviar un mensaje a la cola
mensaje = 'Hola, esto es un mensaje de prueba!'
canal.basic_publish(exchange='', routing_key='cola_de_mensajes', body=mensaje)

print('Mensaje enviado a la cola')

# Cerrar la conexión
conexion.close()
