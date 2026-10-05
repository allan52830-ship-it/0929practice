# Flask Hello World 一頁式網站

這是一個基於 Python Flask 框架建置的現代風格 Hello World 一頁式網站，支援 GitHub Actions CI/CD 與 Render 自動部署。

---

## 專案結構

```text
practice0929/
│
├── .github/workflows/
│   └── deploy.yml          # GitHub Actions CI/CD Pipeline
├── templates/
│   └── index.html          # 一頁式網站前端模板
├── tests/
│   └── test_app.py         # 單元測試
├── app.py                  # Flask 主程式與路由定義
├── pytest.ini              # pytest 設定檔
├── render.yaml             # Render 服務部署設定 (Blueprint)
├── requirements.txt        # 相依套件清單 (含 Flask、gunicorn)
└── README.md               # 專案說明文件
```

---

## 本地開發與啟動

### 1. 建立並啟動虛擬環境 (Virtual Environment)
```bash
python -m venv .venv

# PowerShell
.\.venv\Scripts\Activate.ps1

# CMD
.\.venv\Scripts\activate.bat
```

### 2. 安裝相依套件
```bash
pip install -r requirements.txt
pip install pytest
```

### 3. 執行測試
```bash
pytest
```

### 4. 啟動伺服器
```bash
python app.py
```
啟動後在瀏覽器開啟：[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## CI/CD 與 Render 部署設定

### 運作原理
1. **CI (持續整合)**：當推送到 `main` 分支或發起 Pull Request 時，GitHub Actions 會自動執行環境建置、語法編譯檢查與 `pytest` 單元測試。
2. **CD (持續部署)**：測試通過後，GitHub Actions 會自動呼叫 Render 的 **Deploy Hook** 觸發雲端自動部署。

### 設定步驟
1. 登入 [Render](https://render.com/)，選擇 **New +** > **Web Service**（或 Blueprint 連結本儲存庫）。
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
2. 在 Render 服務頁面點擊 **Settings**，找到 **Deploy Hook** 並複製 Hook 網址。
3. 前往 GitHub 專案儲存庫的 **Settings** > **Secrets and variables** > **Actions**。
4. 點擊 **New repository secret**，新增密鑰：
   - **Name**: `RENDER_DEPLOY_HOOK_URL`
   - **Value**: 貼上步驟 2 取得的 Render Deploy Hook 網址。
5. 之後每次推送到 `main` 分支，GitHub Actions 就會自動測試並無縫部署到 Render！
