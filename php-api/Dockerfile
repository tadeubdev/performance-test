FROM php:8.2-apache

# Instalar o Composer
RUN apt-get update && apt-get install -y curl git unzip && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Definir o diretório de trabalho
WORKDIR /var/www/html

# Copiar os arquivos do projeto
COPY . .

# Instalar as dependências do Composer
RUN composer install

# Configurar o Apache para escutar na porta 8084
RUN sed -i 's/Listen 80/Listen 8084/' /etc/apache2/ports.conf
RUN sed -i 's/:80/:8084/' /etc/apache2/sites-available/000-default.conf

# Expor a porta 8084
EXPOSE 8084
