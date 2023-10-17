# 🐳 Docker

1. Clone or download the repository and go to its directory.
2. Create an **.env** file or rename **.env.example** in **.env** and populate it with all variables from **.env**
   file.
   * In the REDIS_HOST, you need to specify not the local ip, but the name of the redis container, like this: REDIS_HOST=redis.
3. Start the services: `docker-compose up --build -d`
