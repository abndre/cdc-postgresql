# CDC Com Debezium e PostgreSQL

Inicie o projeto docker

```
docker compose up -d
```

Crie o topico no kafka utilizando um post no debezium

```
docker-compose exec debezium curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" \
-d '{
  "name": "my-connector",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "postgres",
    "database.port": "5432",
    "database.user": "postgres",
    "database.password": "postgres",
    "database.dbname": "my-data-gold",
    "database.server.name": "dbserver1",
    "table.include.list": "public.usuarios",
    "database.history.kafka.bootstrap.servers": "kafka:9092",
    "database.history.kafka.topic": "dbhistory.my-connector"
  }
}' http://debezium:8083/connectors

```

Inicie o consumer python

```
pip install -r requirements.txt # utilize env para evitar conflitos
python3 consumer/python_consumer.py
```

Atualize ou envie novos valores para a tabela **usuarios** para ver o consumer consumindo as mensagens
do topico do kafka.