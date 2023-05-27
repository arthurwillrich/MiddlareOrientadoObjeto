import pika

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criação da fila
channel.queue_declare(queue='minha_fila')

# Função para enviar uma mensagem para a fila
def enviar_mensagem(mensagem):
    channel.basic_publish(exchange='', routing_key='minha_fila', body=mensagem)
    print("Mensagem enviada:", mensagem)

# Loop para enviar várias mensagens
while True:
    # Solicita ao usuário uma mensagem para enviar
    mensagem = input("Digite a mensagem para enviar (ou -1 para sair): ")

    if mensagem == "-1":
        break

    # Chama a função enviar_mensagem com a mensagem digitada
    enviar_mensagem(mensagem)

# Fechar a conexão
connection.close()
