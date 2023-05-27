# MiddlareOrientadoObjeto

Lab 03: Middleware Orientado a Mensagens
Implementar uma aplicação no estilo produtor/consumidor, onde alguns processos postam mensagens em fila(s) e outros processos consomem mensagens da(s) fila(s). A escolha da aplicação é livre. Portanto, propor uma aplicação hipotética que se beneficie desse modelo de filas de mensagem faz parte desta atividade.

Você deve utilizar um middleware, servidor ou bilbioteca de filas de mensagens para a sua implementação. Então, o serviço fica em execução e os processos postam e consomem mensagens usando uma API de programação para acesso a este serviço. Há diversas ferramentas que podem ser utilizadas, ex. RabbitMQ, ActiveMQ, Zero MQ, JMS, etc.

Você pode escolher o servidor de filas e linguagem de programação de sua preferência. Note que é possível utilizar diferentes linguagens na implementação de diferentes processos que acessam as filas.

Forma de entrega: (i) Entregar o código-fonte dos processos implementados. (ii) um relatório ou tutorial com o passo a passo da instalação (incluindo a configuração do servidor escolhido, quando necessário) e instruções para a execução dos seus processos.

Esta atividade pode ser realizado em duplas. Informe no relatório/tutorial os nomes e número de matrícula dos participantes.

A seguir eu apresento em alto nível alguns passos para a instalação do RabbitMQ:

Instalação no Linux:
sudo apt-get update
sudo apt-get install erlang
sudo apt-get install rabbitmq-server

- Note que o RabbitMQ utiliza internamente a linguagem Erlang, por isso é necessário instalá-la também.


Execução do serviço:
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
sudo systemctl status rabbitmq-server

- observar os listeners (indica quais protocolos e portas que estão abertas aguardando requisições). Ex. {amqp,5672}  // Advanced Message Queuing Protocol

Execução do plugin para gerenciador de filas via navegador:
sudo rabbitmq-plugins enable rabbitmq_management
sudo systemctl status rabbitmq-server

- Agora no status aparecera também listeners "http" - observe a porta associada aos listeners, pois será usada para acessar o console via navegador

Console de gerenciamento:
abrir navegador - URL: localhost:15672
user/passwd
guest
guest

A partir daqui o serviço e console de gerenciamento estão disponíveis e você pode usar o console para observar o estado das filas e mesmo inspecionar as mensagens depositadas.
