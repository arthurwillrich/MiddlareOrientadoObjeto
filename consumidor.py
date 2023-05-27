import pika

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criação da fila
channel.queue_declare(queue='minha_fila')

# Função de callback para tratar as mensagens recebidas
def callback(ch, method, properties, body):
    print("Mensagem recebida:", body.decode())

# Consumo de mensagens da fila
channel.basic_consume(queue='minha_fila', on_message_callback=callback, auto_ack=True)

# Iniciar o consumo de mensagens
print('Aguardando mensagens...')
channel.start_consuming()
