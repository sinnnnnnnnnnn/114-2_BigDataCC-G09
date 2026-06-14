# 航運資料儀表板：用 Gradio 建立互動式航運資料分析與視覺化儀表板

## 專題資訊

| 項目     | 說明                      |
| ------ | ----------------------- |
| 課程     | 114-2 巨量資料與雲端運算         |
| 組別     | 第 9 組                   |
| 專題形式   | 小組期末專題                  |
| 應用類型   | 航運資料分析儀表板               |
| Web 介面 | Gradio                  |
| 預設網址   | `http://localhost:8080` |

## 組員資訊

| 序號 | 姓名  | 學號         |
| -- | --- | ---------- |
| 組長 | 陳意欣 | C112181102 |
| 組員 | 黃薏庭 | C112181103 |
| 組員 | 蔡异堤 | C112181144 |
| 組員 | 吳宣縈 | C112181149 |
| 組員 | 尤姵瑄 | C112181132 |
| 組員 | 王品儒 | C111181143 |

## 專題簡介

本專題建立一套可重現的航運資料分析流程，將港口營運 CSV 資料透過 Python 進行資料清洗、統計分析與視覺化，再使用 Gradio 封裝為互動式資料分析儀表板。

使用者可以使用系統內建的模擬航運資料，也可以上傳相同欄位格式的 CSV 檔案，快速觀察港口吞吐量、平均滯港時間、船速、延誤率與不同航線的營運表現。

本專題同時使用 Docker 進行容器化部署，使應用程式可以在不同環境中快速執行，並透過 GitHub 進行版本控制與專題成果管理。

## 系統功能

* 使用 `data/raw/sample_shipping_data.csv` 作為示範航運資料
* 支援使用者上傳 CSV 檔案
* 自動檢查必要欄位是否完整
* 自動轉換時間欄位
* 自動補齊缺失值
* 移除不合理數值與重複船舶紀錄
* 產出清洗後資料至 `data/processed/cleaned_shipping_data.csv`
* 提供港口、航線、船舶類型與最低 TEU 的互動篩選
* 顯示 KPI 摘要
* 顯示港口績效表
* 顯示航線績效表
* 顯示篩選後資料
* 使用 Matplotlib 產生資料視覺化圖表
* 使用 Gradio 建立互動式 Web 介面
* 提供 Dockerfile 進行容器化部署

## 專案架構

```text
.
├── data/
│   ├── raw/
│   │   └── sample_shipping_data.csv
│   ├── processed/
│   │   └── cleaned_shipping_data.csv
│   └── README.md
│
├── docker/
│   └── Dockerfile
│
├── docs/
│   └── report.md
│
├── my-topics/
│   └── topic_shipping_dashboard.md
│
├── notebooks/
│   └── shipping_eda.ipynb
│
├── proposal/
│   └── proposal.md
│
├── src/
│   ├── analysis/
│   │   ├── analyze_data.py
│   │   └── clean_data.py
│   ├── app/
│   │   └── gradio_app.py
│   └── utils/
│       └── data_loader.py
│
├── tests/
│   └── test_shipping_dashboard.py
│
├── requirements.txt
└── README.md
```

## 資料欄位說明

| 欄位                 | 說明                            |
| ------------------ | ----------------------------- |
| `timestamp`        | 船舶到港或作業紀錄時間                   |
| `port_name`        | 港口名稱                          |
| `route`            | 航線區域                          |
| `vessel_imo`       | 船舶 IMO 識別碼                    |
| `vessel_type`      | 船舶類型                          |
| `turnaround_hours` | 船舶滯港或週轉時間                     |
| `cargo_teu`        | 裝卸貨櫃量，單位 TEU                  |
| `avg_speed_knots`  | 平均航速，單位節                      |
| `delay_status`     | 船班狀態，包含 `On-Time` 或 `Delayed` |

## 使用技術

| 技術           | 用途               |
| ------------ | ---------------- |
| Python       | 專案主要開發語言         |
| Pandas       | CSV 讀取、資料清洗與分組分析 |
| NumPy        | 缺失值處理與數值運算       |
| Matplotlib   | 資料視覺化圖表          |
| Gradio       | 建立互動式 Web UI     |
| Docker       | 容器化部署            |
| Pytest       | 基本單元測試           |
| Git / GitHub | 版本控制與專題管理        |

## 本機執行方式

### 1. 安裝套件

```bash
pip install -r requirements.txt
```

若系統沒有 `python` 指令，可以改用 `python3`。

### 2. 啟動 Gradio 應用程式

```bash
python -m src.app.gradio_app
```

或使用：

```bash
python3 -m src.app.gradio_app
```

### 3. 開啟網頁

啟動後，在瀏覽器開啟：

```text
http://localhost:8080
```

如果 `8080` 已被其他服務使用，可以改用其他 port：

```bash
GRADIO_SERVER_PORT=8081 python3 -m src.app.gradio_app
```

然後開啟：

```text
http://localhost:8081
```

## Docker 執行方式

### 1. 建立 Docker Image

```bash
docker build -t shipping-analytics-dashboard -f docker/Dockerfile .
```

### 2. 啟動 Docker Container

```bash
docker run --name shipping-dashboard -p 8080:8080 shipping-analytics-dashboard
```

### 3. 開啟系統

```text
http://localhost:8080
```

## 測試方式

執行以下指令進行基本測試：

```bash
pytest
```

## 專題成果

本專題完成一套航運資料分析與視覺化儀表板，能夠從 CSV 資料進行清洗、統計分析、互動篩選與圖表產生。使用者可透過 Gradio 介面操作，不需要撰寫程式即可快速查看航運資料重點。

本系統也透過 Docker 進行容器化部署，符合課程要求中資料分析、資料視覺化、Docker 容器化與 GitHub 版本控制等技術整合目標。

## 專題要求對照表

| 課程要求             | 本專題完成方式                          |
| ---------------- | -------------------------------- |
| Python 資料分析      | 使用 Pandas、NumPy 進行資料清洗、轉換與統計分析   |
| 資料視覺化            | 使用 Matplotlib 產生分析圖表             |
| Docker 容器化       | 撰寫 Dockerfile，將 Gradio 應用程式打包成容器 |
| Git 版本控制         | 使用 GitHub 管理所有程式碼與文件             |
| 選擇性技術            | 使用 Gradio 建立互動式資料分析介面            |
| Jupyter Notebook | 使用 Notebook 進行探索式資料分析            |
| Pytest 測試        | 撰寫基本測試檔案確認功能正常                   |

## 未來改進方向

* 串接真實港口或航運開放資料 API
* 增加船班延誤預測模型
* 新增更多互動式圖表
* 支援多種資料格式，例如 Excel 或 JSON
* 加入資料庫儲存歷史分析結果
* 部署至雲端平台供多人使用

## 授權說明

本專題僅供課程期末專題展示與學習使用。
