# default shell
SHELL = /bin/bash

# Rule "help"
.PHONY: help
.SILENT: help

help:
        echo "Use make [rule]"
        echo "Rules:"
        echo ""
        echo "build           - build application and generate docker image"
        echo "run-db          - run mysql database on docker"
        echo "run-app         - run application on docker"
        echo "stop-app        - stop application"
        echo "stop-db         - stop database"
        echo "rm-app          - stop and delete application"
        echo "rm-db           - stop and delete database"
        echo ""
        echo "k-setup         - init minikube machine"
        echo "k-deploy-db     - deploy mysql on cluster"
        echo "k-build-app     - build app and create docker image inside minikube"
        echo "k-deploy-app    - deploy app on cluster"
        echo ""
        echo "k-start         - start minikube machine"
        echo "k-all           - do all the above k- steps"
        echo "k-stop          - stop minikube machine"
        echo "k-delete        - stop and delete minikube machine"
        echo ""
        echo "check           - check tools versions"
        echo "help            - show this message"

build:
        mvn clean install; \
        docker build --force-rm -t java-k8s .

run-db: stop-db rm-db
        docker run --name mysql57 -p 3306:3306 -d -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_USER=java -e MYSQL_PASSWORD=1234 -e MYSQL_DATABASE=k8s_java mysql/mysql-server:5.7

run-app: stop-app rm-app
        docker run --name myapp -p 8080:8080 -d -e DATABASE_SERVER_NANE=mysql57 --link mysql57:mysql57 java-k8s:latest

stop-db:
        - docker stop mysql57

stop-app:
        - docker stop myapp

k-deploy-db:
        kubectl apply -f k8s/mysql/;

k-build-image:
        mvn clean install; \
        docker build --force-rm -t java-k8s .

