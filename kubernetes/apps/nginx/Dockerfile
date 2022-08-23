	# Setar a imagem do nginx
FROM nginx

	# Autor/Mantenedor
MAINTAINER Jonathan Baraldi

	# Copiar configurações customizadas do diretório atual
COPY nginx_dev.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

COPY certificado/certificado.crt  /etc/ssl/certificado.crt
COPY certificado/certificado.key  /etc/ssl/certificado.key
