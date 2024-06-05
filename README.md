# 新聞爬蟲 API

### 容器化開發

- `VSCode 安裝 Remote Development`
- `VSCode F1 > Dev Containers: Reopen in Container`

### 安裝依賴

- `pip install -r requirements.txt`

### 啟動

- `flask run --host=0.0.0.0`

### API 文件

- `http://localhost:5000/apidocs`

### Q&A

1. 容器化開發共享金鑰

- https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials#_using-ssh-keys
- PS: 如果是 WSL 環境, 需要設定 windows 的 ssh agent, 不繼承 WSL ssh agent
- PS: windows ssh 需要 8.6 以上
