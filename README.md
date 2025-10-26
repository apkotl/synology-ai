# synology-ai

Synology AI tools (N8N, NodeRED, MCP servers)


## Docker-compose commands

```
cd mcp


cd ../red
sudo docker-compose up -d --build node-red-1
sudo docker-compose down
sudo docker-compose down -v
sudo docker-compose down --volumes

docker exec -it nodered node -e "console.log(require('bcryptjs').hashSync('red-password', 8));"


cd ../n8n

sudo docker-compose up -d --build
sudo docker-compose down
sudo docker-compose down -v
sudo docker-compose down --volumes

```

## Other docker commands

```
docker ps
docker volume ls
docker logs nodered
```
