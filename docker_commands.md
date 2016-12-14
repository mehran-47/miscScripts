## search a repository
sudo docker search _repository_  
e.g.: sudo docker search ubuntu  

## pull to repository
sudo docker pull _repository_  
e.g.: sudo docker pull ubuntu  

## list images
sudo docker images  

## rename repository
docker tag _prev-name_:latest _new-name_:latest  
docker tag server:latest myname:latest  
(remove previous tag by)  
sudo docker rmi _prev-name_  

## run image
sudo docker run -it _repository_  
e.g.: sudo docker run -it botubuntu  

## commit image changes
sudo docker commit -m "commit message" _container-id_ _repository_    
e.g.: sudo docker commit -m "installed pip3 and PRAW" 6297281efedb botubuntu  
(you get container id using the command: "docker ps -a")  

## list all docker containers
docker ps -a  
## all running containers
docker ps -a -f status=running  
## list all running and stopped containers, showing only their container id
docker ps -aq  
## remove all containers that are NOT running
docker rm `docker ps -aq -f status=exited`  
