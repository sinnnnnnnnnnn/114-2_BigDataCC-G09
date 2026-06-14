# 資料集說明

本資料夾用於存放「航運資料儀表板」專題所使用的原始資料與清洗後資料。本專題資料主要用於課堂專題展示、資料分析、視覺化與 Gradio 儀表板測試。

## 資料來源

| 項目   | 說明            |
| ---- | ------------- |
| 資料名稱 | 模擬航運與港口物流資料   |
| 來源網址 | 無，專題自行建立      |
| 資料格式 | CSV           |
| 授權方式 | 僅供課堂專題展示與學習使用 |

## 資料用途

本資料集主要用於模擬港口與航運營運情境，讓系統可以進行資料清洗、統計分析與視覺化展示。

資料內容包含船舶到港時間、港口名稱、航線區域、船舶類型、滯港時間、貨櫃量、平均航速與延誤狀態等欄位，可用於分析港口營運效率、船班延誤情形與航線績效。

## 欄位定義

| 欄位名稱               | 資料型態     | 說明                            |
| ------------------ | -------- | ----------------------------- |
| `timestamp`        | datetime | 船舶到港或作業紀錄時間                   |
| `port_name`        | string   | 港口名稱                          |
| `route`            | string   | 航線區域                          |
| `vessel_imo`       | string   | 船舶 IMO 識別碼                    |
| `vessel_type`      | string   | 船舶類型                          |
| `turnaround_hours` | float    | 船舶滯港或週轉時間                     |
| `cargo_teu`        | int      | 裝卸貨櫃量，單位 TEU                  |
| `avg_speed_knots`  | float    | 平均航速，單位節                      |
| `delay_status`     | string   | 準點狀態，包含 `On-Time` 與 `Delayed` |

## 資料夾結構

```text
data/
├── raw/
│   └── sample_shipping_data.csv
├── processed/
│   └── cleaned_shipping_data.csv
└── README.md
```

## 資料夾說明

| 資料夾          | 說明                      |
| ------------ | ----------------------- |
| `raw/`       | 存放原始或示範資料，未經清洗          |
| `processed/` | 存放由系統輸出的清洗後資料           |
| `README.md`  | 說明資料來源、欄位定義、授權方式與使用注意事項 |

## 資料清洗說明

本專題會使用 Python、Pandas 與 NumPy 對資料進行清洗與轉換，主要流程如下：

1. 讀取 `data/raw/sample_shipping_data.csv`
2. 檢查必要欄位是否存在
3. 將 `timestamp` 欄位轉換為 datetime 格式
4. 處理缺失值
5. 移除重複資料
6. 移除不合理數值，例如負數貨櫃量或負數滯港時間
7. 依照港口、航線與船舶類型進行統計分析
8. 將清洗後資料輸出至 `data/processed/cleaned_shipping_data.csv`

## 自訂資料格式要求

如果要上傳自訂 CSV 檔案，欄位名稱需要符合本資料集定義，至少需包含以下欄位：

```text
timestamp, port_name, route, vessel_imo, vessel_type, turnaround_hours, cargo_teu, avg_speed_knots, delay_status
```

若欄位名稱不同，系統可能無法正確讀取、清洗或產生分析圖表。

## 注意事項

* 本資料集為模擬資料，僅供課堂專題展示與系統功能測試使用。
* 本資料不代表真實港口或航運營運狀況。
* 大型資料檔案不建議直接提交到 GitHub。
* 若資料檔案超過 100MB，應使用 `.gitignore` 排除，並在本 README 中提供下載連結或雲端儲存位置。
* 若日後改用政府開放資料或其他公開資料，需補充資料來源網址、下載日期與授權方式。
