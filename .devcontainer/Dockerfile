FROM python:3.10-slim
RUN apt update
RUN apt install git build-essential -y

# 建立開發用戶
RUN adduser --disabled-password --gecos "" --uid 1000 developer
USER developer