# to search a repository
sudo docker search <repository>
e.g.: sudo docker search ubuntu

#to pull to repository
sudo docker pull <repository>
e.g.: sudo docker pull ubuntu

#list images
sudo docker images

#rename repository
docker tag <prev-name>:latest <new-name>:latest
docker tag server:latest myname:latest
(remove previous tag by)
sudo docker rmi <prev-name>

#run image
sudo docker run -it <repository>
e.g.: sudo docker run -it botubuntu

#commit image changes
sudo docker commit -m "commit message" <container-id> <repository>
e.g.: sudo docker commit -m "installed pip3 and PRAW" 6297281efedb botubuntu
(you get container id using the command: "docker ps -a")

#list all docker containers
docker ps -a
#all running containers
docker ps -a -f status=running
#list all running and stopped containers, showing only their container id
docker ps -aq
#remove all containers that are NOT running
docker rm `docker ps -aq -f status=exited`