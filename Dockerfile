# 使用官方的 Python 映像
FROM python:3.10-slim

# 設置工作目錄
WORKDIR /app

# 更新包列表，安裝必要的編譯工具，並清理暫存文件
RUN apt update && apt install -y build-essential && rm -rf /var/lib/apt/lists/*

# 建立執行用戶
RUN adduser --disabled-password --gecos "" --uid 1000 app
RUN chown -R app:app /app
USER app

# 複製 requirements.txt 並安裝依賴
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 複製應用代碼
COPY . .

# 設置環境變數
ENV PATH="/home/app/.local/bin:${PATH}"
ENV UWSGI_PROCESSES=5
ENV UWSGI_HTTP_SOCKET=0.0.0.0:8000

RUN mkdir /app/log

# 使用 uWSGI 運行應用
CMD ["uwsgi", "--ini", "uwsgi.ini"]

