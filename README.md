# attendance-project
in order to run this project you should do :
1.docker pull mysql:latest #downlaod mysql image  from dockerhub
2.docker run --name mysql_container -p 3306:3306 -e MYSQL_ROOT_PASSWORD="amershala" -d mysql #we run  mysql image woth name mysql_container and the passwd..
3.docker build -t attendance_image #we create the image his name is attenadnce image(BUILD הוא משתמש בדוקר פייל)
4.docker-compose up # this command runs the project(using file docker-compose.yml)
5.you can find the web in : localhost:5000 
