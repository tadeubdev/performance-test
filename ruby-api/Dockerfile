FROM ruby:3.2-slim

WORKDIR /app

# Copiar apenas o Gemfile
COPY Gemfile ./

# Instalar as dependências do Gemfile, gerando o Gemfile.lock dentro do container
RUN bundle install

# Copiar o restante da aplicação
COPY . .

EXPOSE 8085

# Iniciar a aplicação Ruby diretamente com Sinatra, sem rackup
CMD ["ruby", "app.rb", "-o", "0.0.0.0", "-p", "8085"]
