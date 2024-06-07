import pika

# Conectar a RabbitMQ
conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()

# Declarar la cola
canal.queue_declare(queue='cola_de_mensajes')

print('Gestor de colas iniciado. Esperando mensajes...')

# Recibir mensajes de la cola
def callback(ch, method, properties, body):
    print('Mensaje recibido:', body)
    # Procesar el mensaje aquí
    subscriptor(body)

canal.basic_consume(queue='cola_de_mensajes', on_message_callback=callback, auto_ack=True)

# Iniciar el bucle de recepción de mensajes
canal.start_consuming()