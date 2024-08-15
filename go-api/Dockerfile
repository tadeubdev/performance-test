# Etapa de construção
FROM golang:1.20-alpine AS build

WORKDIR /app

# Copie o código do projeto
COPY . .

# Inicialize o módulo Go e baixe as dependências
RUN go mod init go-api
RUN go mod tidy

# Compile o binário
RUN go build -o go-api

# Etapa de produção
FROM alpine:latest

WORKDIR /root/

COPY --from=build /app/go-api .

EXPOSE 8081

CMD ["./go-api"]