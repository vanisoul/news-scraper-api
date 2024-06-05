# 用於加入反向代理測試

1. 進入 ./deploy-demo 執行 `docker compose up -d`
2. 使用 linux curl 測試 `curl --resolve mynewsapi.local:443:127.0.0.1 https://mynewsapi.local/scrape --insecure`