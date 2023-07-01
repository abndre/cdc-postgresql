from kafka import KafkaConsumer

# Configurações do Kafka
bootstrap_servers = 'localhost:9092'
topic_name = 'dbserver1.public.usuarios'

# Cria o consumidor do Kafka
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    group_id='my-group',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: x.decode('utf-8')
)

# Loop de consumo de mensagens
for message in consumer:
    print(message.value)
