# De onde deve ser pega a imagem e a versão. Nesse caso do repositório padrão do Docker, a imagem do node

FROM node:14.20.0-alpine
# FROM daveamit/node-alpine-grpc

COPY ./package-lock.json /package-lock.json
COPY ./package.json /package.json

# Autor/Mantenedor
MAINTAINER Jonathan Baraldi

# Prover camada de cached para os módulos do Node
RUN cd /tmp && npm install

RUN mkdir -p /src 
	# Instalar MariaDB SQL e rodar o script para injetar o SQL

RUN npm install mysql
	# Definir diretório de trabalho
WORKDIR /src
ADD . /src

	# Expor porta 80
EXPOSE  8080

	# Rodar o app usando nodemon
CMD ["node", "/src/index.js"]