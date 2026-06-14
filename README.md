# 114-2 巨量資料與雲端運算 期末專題

# 航運資料儀表板 (Shipping & Port Logistics Dashboard)

## 專題資訊

| 項目 | 說明 |
| --- | --- |
| 課程 | 114-2 巨量資料與雲端運算 |
| 組別 | 第 9 組 |
| 專題名稱 | 航運資料儀表板：用 Gradio 建立互動式航運資料分析與視覺化儀表板 |
| 專題形式 | 小組專題 |
| 應用類型 | 資料分析儀表板 |
| 主要資料 | `data/raw/sample_shipping_data.csv` |
| 啟動方式 | 本機 Python 或 Docker |
| Web 介面 | Gradio |
| 預設網址 | `http://localhost:8080` |

## 組員資訊
| 序號 | 姓名 | 學號 |
| --- | --- | --- |
| 組長 | 陳意欣 | C112181102 |
| 組員 | 黃薏庭 | C112181103 |
| 組員 | 蔡异堤 | C112181144 |
| 組員 | 吳宣縈 | C112181149 |
| 組員 | 尤姵瑄 | C112181132 |
| 組員 | 王品儒 | C111181143 |

本專案為「114-2 巨量資料與雲端運算」期末成果，主攻「航運資料儀表板」之開發。  
核心目標在於運用 Python 生態系，對全球主要航線與港口的物流數據進行 ETL（提取、清洗、轉換）與統計建模。透過 Pandas 與 NumPy 優化資料結構後，整合 Matplotlib 繪製關鍵績效指標（KPI）圖表，並以 Gradio 封裝為輕量級網頁服務，最後透過 Docker 實現「一鍵部署、跨平台運行」的雲端與本機環境重現。

本系統內建全球模擬航運資料，同時開放彈性的 CSV 上傳機制。使用者可透過極簡的網頁介面，即時切換不同的航線、港口、貨櫃類型，藉此剖析船舶滯港時數、準點率趨勢及貨量分布。

## 系統截圖

以下為 Gradio 航運儀表板的運行生態圖，涵蓋全球主要樞紐港口篩選、物流 KPI 欄位切換、動態圖表生成區及動態資料清洗預覽。

![航運資料儀表板系統截圖](docs/screenshots/shipping_dashboard_home.png)

## 專題在做什麼

全球貿易高達八成仰賴海運，港口與航線的營運效率（如：船舶排隊時間、貨櫃翻轉率）會直接影響全球供應鏈。然而，傳統航運日誌與報表多為破碎、未結構化的超大型 CSV 檔，管理人員難以一眼看出潛在的物流瓶頸。

本專題打造了一套標準化的海運大數據處理管線（Data Pipeline）：

```text
航運營運 CSV
→ Python 串流讀取
→ Pandas 自動化異常值清洗與標準化
→ NumPy 計算港口轉運效率與極值
→ Matplotlib 輸出多維度商務圖表
→ Gradio 渲染低程式碼（Low-code）互動網頁
→ Docker 鏡像打包與微服務化
→ 瀏覽器即時監控與決策支援

```

本專題的精髓在於展示如何將底層的資料科學技術，包裝成非技術人員也能輕鬆操作的端到端（End-to-End）實用商務系統。

## 專題動機

當前全球航運面臨港口擁擠、航線變更及運價波動等不確定因素，供應鏈分析師急需精準的數據支持。然而，第一線蒐集到的原始航運數據常面臨以下痛點：各國港口代碼（UN/LOCODE）不一致、船舶抵港時間格式錯亂、貨櫃噸位缺失或輸入重複。

本專題旨在建立一個自動化容錯與視覺化系統。透過後台的清洗演算法，將混亂的航運日誌梳理成結構清晰的統計報表，並透過互動式網頁，讓調度員與管理階層無需撰寫 SQL 或 Python 程式碼，就能動態洞察各航線的營運體質與延誤主因。

## 使用技術

| 技術 | 用途 |
| --- | --- |
| Python | 專案核心開發語言 |
| Pandas | 航運巨量資料操作、港口分組（GroupBy）聚合與時序資料重採樣 |
| NumPy | 船速與滯港時間之矩陣運算、百分位數與離群值偵測 |
| Matplotlib | 繪製航線準點率折線圖、港口吞吐量長條圖及貨櫃類型圓餅圖 |
| Gradio | 快速構建具備滑桿、下拉選單與圖表輸出的響應式 Web UI |
| Docker | 撰寫環境配置檔，包裝所有依賴套件，解決跨平台部署衝突問題 |
| Jupyter Notebook | 前期對航運原始數據進行特徵工程與探索性資料分析 (EDA) |

## 課程要求對照

| 課程要求 | 本專案完成內容 |
| --- | --- |
| Python 資料分析 | 利用 Pandas & NumPy 進行船舶噸位、滯港時數的統計摘要與各港口績效分組 |
| 資料視覺化 | 運用 Matplotlib 生成時間序列趨勢圖、樞紐港口對比圖及貨量結構分析圖 |
| 互動式應用 | 搭建 Gradio 介面，支援動態篩選航線、自訂時間軸區間與 CSV 檔案上傳解析 |
| Docker 容器化 | 提供完整 `docker/Dockerfile`，預建 Port `8080` 映像檔，確保一鍵運行 |
| 文件完整度 | 交付專案提案書、架構說明、動態資料字典（Data Dictionary）與最終成果報告 |
| 可重現性 | 附帶明確的 `requirements.txt`、模擬供應鏈測試資料及標準 Docker CLI 指令 |

## 系統功能

* **雙資料源切換**：支援系統內建的 `sample_shipping_data.csv` 或用戶自行上傳之航運日誌。
* **欄位合規性校驗**：上傳時自動偵測是否包含 IMO 船舶編號、港口、時間等必備維度。
* **雙狀態資料流檢視**：同時預覽前 10 筆「原始未修補」與「清洗轉換後」的資料對照。
* **時間序列標準化**：將各國混合的抵港/離港時間（ETA/ETD）統一轉換為 ISO 8601 標準 datetime 格式。
* **精準缺失值衍生**：數值型欄位（如船速、載重量）缺失時，自動以該航線平均值填補；缺失港口名稱則歸類為 `Unknown Port`。
* **物流邏輯除錯**：自動剔除離港時間早於抵港時間的邏輯錯誤資料，並過濾重複的報關單號。
* **自動化實體輸出**：清洗完成的乾淨資料將自動導出至 `data/processed/cleaned_shipping_data.csv`。
* **多維度商業決策分析**：提供全航線描述性統計、單一港口擁擠度評估、以及各月份物流尖峰預測。
* **跨平台環境相容**：完美支援 Linux/Mac/Windows 環境之 Docker 部署。

## 專案架構

```text
114-2_BigDataCC_ShippingDashboard/
│
├── README.md                          # 專案主說明文件
│
├── my-topics/
│   └── topic_shipping_dashboard.md    # 選題可行性與技術評估
│
├── proposal/
│   └── proposal.md                    # 航運專題提案計畫書
│
├── data/
│   ├── raw/
│   │   └── sample_shipping_data.csv   # 原始航運模擬資料
│   ├── processed/
│   │   └── cleaned_shipping_data.csv  # ETL 後的乾淨航運資料
│   └── README.md                      # 資料欄位定義與來源說明
│
├── notebooks/
│   └── shipping_eda.ipynb             # 航運數據探索與圖表原型實驗
│
├── src/
│   ├── __init__.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── clean_data.py              # 航運資料清洗與時間格式校正核心
│   │   └── analyze_data.py            # 港口吞吐量、延誤率統計運算
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   └── gradio_app.py              # Gradio 前端介面與佈局配置
│   │
│   └── utils/
│       ├── __init__.py
│       └── data_loader.py             # 負責處理本機與容器路徑的資料加載器
│
├── docker/
│   └── Dockerfile                     # 容器化建置設定檔
│
├── docs/
│   ├── report.md                      # 期末終端專題報告
│   ├── screenshots/
│   │   └── shipping_dashboard_home.png # 介面截圖存放處
│
├── tests/
│   └── test_shipping_dashboard.py     # 測試物流運算邏輯之單元測試
│
├── .gitignore
└── requirements.txt                   # 專案相依套件清單

```

## 主要程式說明

| 檔案 | 說明 |
| --- | --- |
| `my-topics/topic_shipping_dashboard.md` | 分析引入航運大數據在雲端運算架構下的可行性與價值。 |
| `proposal/proposal.md` | 詳細規劃航運專案的時程、預期 KPI 成果以及數據管線設計。 |
| `src/utils/data_loader.py` | 兼容層設計，動態識別本機相對路徑或 Docker 磁碟區（Volume）之 CSV 資料。 |
| `src/analysis/clean_data.py` | 專責異常物流數據剔除、計算實際航行學時，並補齊漏填的船舶基本規格。 |
| `src/analysis/analyze_data.py` | 封裝進階分析演算法，計算港口平均滯港時間、最繁忙航線及準點率分布。 |
| `src/app/gradio_app.py` | 主網頁程式，將後端分析模組與 Matplotlib 畫布綁定至 Gradio 監聽元件中。 |
| `docker/Dockerfile` | 基於輕量級 Python 鏡像，配置亞太區標準時間，解決圖表中文字型碎裂問題。 |
| `notebooks/shipping_eda.ipynb` | 供開發團隊快速驗證群聚分析（Clustering）港口特徵的實驗沙盒。 |
| `docs/report.md` | 統整專題產出，包含系統效能評估與航運洞察結論。 |

## 資料來源與欄位說明

專案內建之基準數據存放於：

```text
data/raw/sample_shipping_data.csv

```

### 關於模擬資料

為確保期末展示（Demo）期間不受各國港口 API 封鎖、傳輸延遲或商業機密限制，本專案依據國際航運物流常見報表格式，自主生成了一份精準的**自建模擬供應鏈資料集**。這能完美模擬真實世界中港口塞港與航線延誤的特徵，提供高度可預測的系統展示。

### 資料規格概況

* **總資料筆數**：100 筆（涵蓋多班次往返）。
* **時間維度**：2026-05-01 至 2026-05-31（完整月份航線日誌）。
* **涵蓋樞紐港口**：5 個全球核心貿易港。
* **模擬港口名單**：Tokyo、Shanghai、Singapore、Rotterdam、Los Angeles。

### 欄位字典

| 欄位名稱 | 說明 | 單位或格式 |
| --- | --- | --- |
| `timestamp` | 船舶報到或離港時間 | `YYYY-MM-DD HH:MM` |
| `port_name` | 停靠樞紐港口名稱 | Tokyo, Shanghai, Singapore, Rotterdam, Los Angeles |
| `vessel_imo` | 國際海事組織船舶唯一識別碼 | `IMOXXXXXXX` (七位數字) |
| `turnaround_hours` | 船舶滯港/週轉時間（從抵港到出港） | 小時 (Hours) |
| `cargo_teu` | 本次裝卸之標準貨櫃量 | TEU (20呎標準櫃換算單位) |
| `avg_speed_knots` | 該航段平均航速 | 節 (Knots) |
| `delay_status` | 班期準點判定 | On-Time / Delayed |

---

## 若要對接真實航運資料

本專案架構具備高度擴充性。若未來欲投入商業實用，建議對接以下國際公開或半公開之航運大數據源：

### 推薦數據源

| 數據源名稱 | 說明 | 適合獲取的特徵 |
| --- | --- | --- |
| **MarineTraffic / AIS API** | 全球船舶自動識別系統（AIS）即時廣播訊號 | 動態經緯度、即時航速、預估抵港時間（ETA） |
| **UNCTADstat (聯合國貿發會議)** | 國際海運與港口吞吐量年度統計數據庫 | 全球各大洲長週期的航運指數、港口績效基準 |
| **航港單一窗口服務平臺 (MTNet)** | 臺灣交通部航港局之海運進出港與報關公開資料 | 臺灣各港口（高雄、基隆等）真實船舶進出港時間戳與載重 |

### 開發串接流程

1. 向 AIS 數據商或公開平台申請開發者 API Token。
2. 利用 Python `requests` 模組，定時抓取指定港口群的 JSON 格式進出港動態。
3. 透過自定義的轉換器（Adapter），將真實資料中的欄位（如 `mmsi`、`vessel_speed`）映射至本專案標準欄位（`vessel_imo`、`avg_speed_knots`）。
4. 本系統之 Gradio UI 具備「上傳 CSV」功能，使用者可直接將匯出的真實資料上傳，完全不需改動任何底層統計程式。

---

## 資料清洗管線（Pipeline）

本系統的 `clean_data.py` 模組依序執行下列自動化程序：

1. **結構校驗**：檢查輸入資料是否包含 `vessel_imo` 與 `port_name` 等主鍵。
2. **型態導正**：將字串型態的時間軸，利用 `pd.to_datetime()` 轉為標準時序物件。
3. **異常值過濾**：剔除航速大於 40 節（不合常理）或滯港時數為負值的邏輯死角。
4. **缺失值智能插補**：貨櫃量（TEU）缺失時，採用該港口當月的平均裝卸量進行中位數補齊。
5. **重複資料清洗**：比對船舶編號與時間戳，自動刪除重複上報的日誌紀錄。
6. **實體落盤**：將清洗後的優質數據寫入 `processed/` 目錄，供後續統計模組調用。

## 視覺化圖表類型

為了讓跨國用戶在任何作業系統上皆能流暢讀取圖表，本專案刻意使用**英文圖表標籤**與通用字型，全面排除 Docker 容器內常發生的中文字型拼貼破裂問題：

* **Trend Line Chart (時序趨勢圖)**：橫軸為日期，縱軸為平均滯港時數，用以監控特定港口是否有塞港惡化傾向。
* **Station Average Bar Chart (港口吞吐對比圖)**：比較各個樞紐港口在特定時間區間內的總裝卸貨櫃量（TEU）。
* **Monthly Average Line Chart (航速效能變動圖)**：追蹤不同月份、不同航線上船舶平均航速的節能或延誤趨勢。

---

## 本機執行方式

請在專案根目錄（包含 `requirements.txt` 的路徑）啟動終端機：

```bash
# 切換至專案根目錄
cd 114-2_BigDataCC_ShippingDashboard

# 安裝相依套件（建議先開啟虛擬環境）
pip install -r requirements.txt

# 以模組化方式啟動 Gradio UI
python -m src.app.gradio_app

```

啟動成功後，終端機會輸出 local 網址，請在瀏覽器輸入：

```text
http://localhost:8080

```

---

## Docker 容器化部署步驟

本專案已完美容器化，可脫離本機 Python 環境限制。

### 1. 檢視本機環境

確保 Docker Desktop 處於運行狀態：

```bash
docker --version

```

### 2. 建置航運分析映像檔

```bash
docker build -t shipping-analytics-dashboard -f docker/Dockerfile .

```

### 3. 實例化啟動容器

```bash
docker run --name shipping-container -p 8080:8080 shipping-analytics-dashboard

```

### 4. 開啟 Web UI

打開瀏覽器導向 `http://localhost:8080`，即可進入湛藍航運風格的互動式大數據管理後台。

### 5. 資源回收與停止

```bash
# 停止容器運行
docker stop shipping-container

# 刪除已停止的容器實例
docker rm shipping-container

```

---

## 系統開啟後的操作動線

當你進入 `http://localhost:8080` 後：

1. **模組切換**：在左側側邊欄或上方分頁，選擇要分析「內建基準物流資料」或「自行導入企業日誌」。
2. **參數配置**：利用下拉選單過濾出特定樞紐港口（如 `Singapore`），並利用滑桿調整欲觀察的最小貨櫃裝卸量。
3. **選定指標**：選擇欲視覺化的關鍵指標（例如滯港小時數 `turnaround_hours`）。
4. **一鍵觸發**：點擊 **"Execute Logistics Analysis"**。
5. **洞察呈現**：
* 「Raw Data View」與「Cleaned Data View」分頁將呈現 ETL 前後的資料矩陣。
* 系統正中央將即時渲染 Matplotlib 高清圖表，清楚指出哪一個港口正在發生供應鏈瓶頸。



```

```
| `src/analysis/analyze_data.py` | 產生整體統計、港口/船型統計、月份平均與極值分析 |
| `src/app/gradio_app.py` | 建立 Gradio Web UI，整合資料讀取、清洗、分析與圖表顯示 (監聽 Port 8080) |
| `docker/Dockerfile` | 建立 Docker 映像檔，安裝 Python 套件與中文字型，並對外暴露 Port 8080 |
| `notebooks/exploration.ipynb` | 用 Jupyter Notebook 進行初步航運資料探索 |
| `docs/report.md` | 期末報告初稿 |

## 資料來源與欄位說明

本專案的範例資料位於：

```text
data/raw/sample_shipping_data.csv

```

這份 CSV 不是從特定航運機構直接下載的真實營運資料，而是本專題為了 Demo 與測試自行建立的模擬資料（自建模擬資料）。資料格式參考航運與港口大數據常見指標設計，主要用於展示資料清洗、統計分析與視覺化流程。

建立模擬資料的原因：

* 期末 Demo 時可確保每次執行都有穩定、不中斷的資料流。
* 欄位名稱能完全配合本系統的清洗與分析流程。
* 不需要商業 API Key，也不會受到即時物流資料延遲、缺值或格式變動影響。
* 資料量適中，適合課堂展示與測試。

資料概況：

| 項目 | 內容 |
| --- | --- |
| 資料筆數 | 75 筆 |
| 日期範圍 | 2026-03-01 至 2026-03-15 |
| 港口數量 | 5 個 |
| 港口名稱 | Keelung、Taichung、Kaohsiung、Shanghai、Singapore |
| 缺失值 | 範例資料目前無缺失值，系統仍保留缺失值處理機制 |

| 欄位名稱 | 說明 | 單位或格式 |
| --- | --- | --- |
| `date` | 觀測/統計日期 | `YYYY-MM-DD` |
| `port` | 港口名稱 | Keelung, Taichung, Kaohsiung, Shanghai, Singapore |
| `vessel_type` | 船舶類型 | Container (貨櫃船), Bulk Carrier (散裝船), Tanker (油輪) |
| `cargo_volume_teu` | 貨櫃吞吐量 | TEU (二十呎標準貨櫃) |
| `freight_index` | 運價指數 | 點 (參考 CCFI / BDI 趨勢) |
| `turnaround_time_hours` | 船舶滯港/週轉時間 | 小時 |
| `fuel_consumption_tons` | 每日燃油消耗量 | 噸 |

## 如果要抓真實資料

若未來要改成真實航運觀測與物流資料，可以優先使用國內外交通部或國際航運交易所的開放資料。

建議資料來源：

| 來源 | 說明 | 適合用途 |
| --- | --- | --- |
| 臺灣航港局航港發展資料庫 | 國內主要港口進出港、貨物吞吐量等官方統計 | 臺灣港口歷史營運分析 |
| 上海航運交易所 (SSE) | 發布貨櫃運價指數（SCFI、CCFI） | 貨櫃航運市場運價趨勢分析 |
| 波羅的海交易所 (Baltic Exchange) | 發布散裝航運波羅的海原油指數（BDI） | 散裝航運與大宗商品市場分析 |
| 交通部 CPTD 運輸資料流通服務平臺 | 提供國內航運、港口與船舶即時/歷史資料 API | 自動化數據串接與定時更新 |

真實資料串接流程：

1. 到 TDX 運輸資料流通服務平臺或相關開放資料網頁註冊帳號。
2. 取得 API 授權金鑰 (Client ID / Client Secret)。
3. 使用 Python `requests` 讀取 API 回傳的 JSON 或 CSV 資料。
4. 將官方定義的欄位（如港口代碼、進港時間）轉成此專案需要的欄位名稱。
5. 儲存成 CSV，例如 `data/raw/real_shipping_data.csv`。
6. 在 Gradio 介面選擇上傳該 CSV，或修改 `load_sample_data()` 改讀真實資料。

Python 抓取範例：

```python
import os
import pandas as pd
import requests

# 假設串接某航運運價指數 API
API_KEY = os.getenv("SHIPPING_API_KEY")
URL = "[https://api.shippingdata.example.com/v1/market/freight-index](https://api.shippingdata.example.com/v1/market/freight-index)"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

params = {
    "start_date": "2026-01-01",
    "end_date": "2026-03-15",
    "format": "json"
}

response = requests.get(URL, headers=headers, params=params, timeout=30)
response.raise_for_status()
data = response.json()

# 觀察 API 回傳結構並整理成 DataFrame
records = data["data"]["index_records"]
df = pd.json_normalize(records)

# 依照本專案欄位重新命名
df.rename(columns={
    "reportDate": "date",
    "portName": "port",
    "indexValue": "freight_index"
}, inplace=True)

print(df.head())

```

欄位轉換方向：

| 官方資料常見欄位 | 本專案欄位 |
| --- | --- |
| 港口名稱 / 港口代碼 | `port` |
| 統計基準日期 / 船舶靠泊日期 | `date` |
| 貨櫃裝卸量 (TEU) / 貨物噸位 | `cargo_volume_teu` |
| SCFI / CCFI / BDI 指數數值 | `freight_index` |
| 船舶在港時間 / 靠泊學時 | `turnaround_time_hours` |

注意：不同類型的航運資料集（如散裝 vs 貨櫃）指標不盡相同。如果真實來源缺少貨櫃吞吐量 `cargo_volume_teu`（例如散裝航運），正式做法應將該欄位改為貨物噸位，或修改程式讓該欄位在儀表板中變成選填。

## 資料清洗流程

系統在分析前會先執行以下清洗步驟：

1. 檢查資料是否包含必要欄位。
2. 將 `date` 欄位轉成 datetime 格式。
3. 將數值欄位（吞吐量、運價、滯港時間等）轉成 numeric 格式。
4. 移除無法轉換日期的資料列。
5. 數值欄位缺失值使用該欄位平均值補齊。
6. `port` 與 `vessel_type` 欄位缺失值填入 `Unknown`。
7. 移除重複資料。
8. 依照 `date` 與 `port` 排序。
9. 儲存清洗後資料到 `data/processed/cleaned_shipping_data.csv`。

## 統計分析與圖表

系統目前支援以下分析欄位：

* `cargo_volume_teu`
* `freight_index`
* `turnaround_time_hours`
* `fuel_consumption_tons`

支援的分析結果包含：

* 整體統計摘要：市場平均值、標準差、最大/小值與四分位數。
* 港口營運與船型分組統計：依照港口或船舶類型比較不同指標的效率與表現。
* 月份趨勢分析：觀察運價或吞吐量在不同月份的季節性變化。
* 極值分析：找出指定指標的最高峰（如塞港嚴重的最大滯港時間）與最低谷。

支援的圖表類型包含：

* `Trend Line Chart`：依日期顯示運價指數或吞吐量變化趨勢。
* `Port Average Bar Chart`：比較不同港口間的平均吞吐量或滯港時間。
* `Monthly Average Line Chart`：顯示特定指標的月份平均與季節波動。

圖表座標軸與標題主要使用英文，目的是降低 Docker 或不同作業系統中文字型顯示問題。

## 本機執行方式

以下指令請在專案根目錄執行：

```bash
cd 114-2_BigDataCC_ShippingDashboard

```

安裝套件：

```bash
pip install -r requirements.txt

```

啟動 Gradio App：

```bash
python -m src.app.gradio_app

```

啟動後在瀏覽器開啟：

```text
http://localhost:8080

```

## Docker 部署到開啟系統

本專案已提供 `docker/Dockerfile`，容器啟動後會執行 Gradio App，並透過 `8080` port 對外提供服務。

### 1. 確認 Docker 已啟動

先開啟 Docker Desktop，接著在終端機確認 Docker 可用：

```bash
docker --version

```

### 2. 建立 Docker 映像檔

請在專案根目錄執行：

```bash
docker build -t shipping-data-dashboard -f docker/Dockerfile .

```

這個指令會根據 `docker/Dockerfile` 建立名為 `shipping-data-dashboard` 的映像檔。

### 3. 啟動 Docker 容器

一般執行方式：

```bash
docker run -p 8080:8080 shipping-data-dashboard

```

如果想指定容器名稱，方便後續停止容器，可以使用：

```bash
docker run --name shipping-dashboard-demo -p 8080:8080 shipping-data-dashboard

```

### 4. 開啟系統

容器啟動後，在瀏覽器輸入：

```text
http://localhost:8080

```

看到「航運資料儀表板」頁面後，即可開始操作系統。

### 5. 停止容器

如果是直接在終端機執行 `docker run`，可以按 `Ctrl + C` 停止。

如果有指定容器名稱，可以另開一個終端機執行：

```bash
docker stop shipping-dashboard-demo

```

需要移除容器時可執行：

```bash
docker rm shipping-dashboard-demo

```

## 系統開啟後會看到什麼

開啟 `http://localhost:8080` 後，頁面會顯示具有航運與工業物流風格的 Gradio 儀表板。上方可選擇資料來源、上傳自訂航運 CSV、選擇分析指標、篩選特定港口/船型與圖表類型；按下分析按鈕後，下方會顯示數據資料表、營運摘要與圖表。

主要頁籤包含：

* 原始資料預覽：顯示上傳或範例 CSV 的前 10 筆航運原始數據。
* 清洗後資料預覽：顯示轉換與清洗後（處理完缺值、極值）的前 10 筆資料。
* 統計摘要：顯示整體市場統計、港口/船型分組效能統計與營運極值。
* 視覺化圖表：顯示 Matplotlib 產生的市場趨勢圖或港口效率比較圖。

## Gradio 介面操作流程

1. 選擇資料來源：`範例資料` 或 `上傳 CSV`。
2. 如果選擇 `上傳 CSV`，請上傳包含必要航運欄位的 CSV 檔案。
3. 選擇分析指標，例如貨櫃吞吐量、運價指數、滯港時間或燃油消耗。
4. 選擇篩選條件：可選擇全部港口/船型或單一港口/船型。
5. 選擇圖表類型（趨勢折線圖、港口長條圖等）。
6. 按下 `分析 / 更新儀表板`。
7. 查看原始與清洗後資料、營運統計摘要與 Matplotlib 視覺化圖表。

## 錯誤處理

系統已加入基本錯誤處理：

* 如果選擇上傳資料但沒有提供檔案，系統會提示使用範例資料或上傳 CSV。
* 如果航運 CSV 缺少必要欄位（如 `port` 或 `cargo_volume_teu`），系統會顯示缺少哪些欄位。
* 如果日期欄位格式混亂無法轉換，該資料列會在清洗時自動移除。
* 如果清洗過後符合條件的資料為空，系統會提示篩選範圍或資料格式可能有誤。
* 如果選擇的分析指標不存在，系統會提示目前的可用欄位。

## 專題成果

本專題完成以下成果：

* 建立航運與港口營運指標模擬資料集。
* 完成 Python 資料讀取、清洗與航運統計分析模組。
* 完成 Matplotlib 航運趨勢與比較視覺化圖表。
* 完成 Gradio 互動式航運數據儀表板。
* 完成 Docker 容器化部署。
* 完成期末報告初稿。

相關文件：

* 專題提案：`proposal/proposal.md`
* 個人選題探索：`my-topics/topic_shipping_dashboard.md`
* 資料說明：`data/README.md`
* 期末報告：`docs/report.md`

## 注意事項

* `data/raw/sample_shipping_data.csv` 是展示用模擬資料，不代表真實國際航線與港口數據。
* 若改用真實資料，請在 `data/README.md` 補上資料來源網址、下載日期、授權方式（如 TDX 授權）與欄位轉換對照表。
* `data/processed/cleaned_shipping_data.csv` 會在系統執行後產生，並已設定在 `.gitignore` 中以免重覆提交。
* 上傳自訂 CSV 時，欄位名稱與大小寫需要與本專案規範完全一致。
* Dockerfile 會安裝 Noto CJK 字型，確保 Linux 容器環境中的中文字型在 Matplotlib 產圖時顯示正常。
* Gradio App 已設定 `server_name="0.0.0.0"` 與 `server_port=8080`，可確保 Docker 端口映射後正常在外部瀏覽器存取。

```

```
