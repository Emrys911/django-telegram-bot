FROM ubuntu:latest
LABEL authors="user"

ENTRYPOINT ["top", "-b"]
# Используем официальный образ Nginx
FROM nginx:latest

# Копируем конфигурационный файл Nginx в контейнер
COPY nginx.conf /etc/nginx/nginx.conf

# Открываем порт 80 для внешних подключений
EXPOSE 80
