create topic

```
docker exec broker \
kafka-topics --bootstrap-server broker:9092 \
             --create \
             --topic orders
```

publish message

```
docker exec --interactive --tty broker \
kafka-console-producer --bootstrap-server broker:9092 \
                       --topic orders
```

read message

```
docker exec --interactive --tty broker \
kafka-console-consumer --bootstrap-server broker:9092 \
                       --topic orders \
                       --from-beginning
```