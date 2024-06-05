# 新聞爬蟲 API

### 容器化開發

- `VSCode 安裝 Remote Development`
- `VSCode F1 > Dev Containers: Reopen in Container`

### 安裝依賴

- `pip install -r requirements.txt`

### 啟動

- 開發環境 flask : `flask run --host=0.0.0.0`
- 發布環境 uwsgi : `UWSGI_PROCESSES=5 UWSGI_HTTP_SOCKET=0.0.0.0:5000 uwsgi --ini uwsgi.ini`

### API 文件

- `http://localhost:5000/apidocs`

### 反向代理範例
[連結](./deploy-demo/)

### Q&A

1. 容器化開發共享金鑰

- https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials#_using-ssh-keys
- PS: 如果是 WSL 環境, 需要設定 windows 的 ssh agent, 不繼承 WSL ssh agent
- PS: windows ssh 需要 8.6 以上
