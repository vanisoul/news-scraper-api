# 使用較輕量的 Python 基礎映像
FROM python:3.10-slim

# 建立工作目錄
WORKDIR /app

# 複製 requirements.txt 並安裝 Python 套件
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案中的所有檔案
COPY . .

# 設定環境變數
ENV FLASK_APP=run.py

# 開放 Flask 預設埠
EXPOSE 5000

# 使用flask指令啟動應用程式
CMD ["flask", "run", "--host=0.0.0.0"]
