# attendance-project
in order to run this project you should do :
1.docker pull mysql:latest #downlaod mysql image  from dockerhub
2.docker run --name mysql_container -p 3306:3306 -e MYSQL_ROOT_PASSWORD="amershala" -d mysql
3.docker build -t attendance_image
4.docker-compose up
5.you can find the web in : localhost:5000 
