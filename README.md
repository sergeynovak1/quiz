# 🐳 Docker

1. Clone or download the repository and go to its directory.
2. Create an **.env** file or rename **.env.example** in **.env** and populate it with all variables from **.env**
   file.
3. Start the services: `docker-compose up --build -d`
4. follow the link http://127.0.0.1:9999/docs#/default/get_questions_get_questions__post, there is already a request template in the swager
 
## Request example

POST /get_questions:
      {
        "questions_num": 20
      }
