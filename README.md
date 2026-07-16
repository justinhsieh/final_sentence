# Final Sentence (終極判決)

**Final Sentence** 是一款將「極限打字」與「俄羅斯輪盤 (Russian Roulette)」完美融合的高壓生存打字遊戲。
在這裡，打字不只是精準度的考驗，更是一場關乎生死的賭局。在每關 240 秒的緊迫倒數與無情敲擊聲中，任何一次手滑、錯字都可能將你推向左輪手槍的槍口。

本專案採用類似 **MVC (Model-View-Controller) 的架構設計**，並原生支援 **區域網路 (LAN) 多人即時連線對戰**、**持久化本地任務系統**與**排行榜系統**。

---

## 🎮核心遊戲機制 (Gameplay Mechanics)

1. **五重極限審判**：
   * 玩家必須在單場遊戲中，連續正確輸入 **5 篇預設或自訂文本**。
   * 每篇文本有獨立的 **240 秒倒數計時**。若計時歸零，無情大衣男子會直接開槍，挑戰失敗。
2. **三擊輪盤規則 (Three-Strike Russian Roulette)**：
   * 遊戲中允許累積 **3 次打字失誤**（Strikes）。
   * 當失誤滿 3 次時，介面會被凍結，隨即觸發**俄羅斯輪盤抽獎**：
     * 系統隨機裝填一顆子彈並瘋狂旋轉彈巢。
     * 轉動停止後扣動扳機。
     * **中彈** ：大衣男子扣動扳機，遊戲直接結束 (YOU ARE DEAD!!)。
     * **倖存** ：發出清脆的「喀噠」空槍聲。玩家失誤次數歸零，但文本會**強制回滾 (Reset) 至當前行開頭**，且下一次觸發輪盤時，中彈機率將隨裝填子彈數增加而急遽上升！
3. **即時連線淘汰賽**：
   * 支援私人區域網路 (LAN) 房。所有玩家在同一時間輸入相同的 5 篇文本。
   * 第一個無失誤通關所有文本的玩家獲勝。若其他玩家皆中彈身亡，最後的倖存者自動奪冠！

---

## 🛠️ 系統架構與模組設計 (Architecture & Modules)

本專案將**狀態管理 (Model)**、**視覺渲染 (View)** 與 **業務邏輯控制 (Controller)** 徹底分離，架構極其清晰，便於二次開發與擴充。

### 📂 專案目錄結構

```text
.
├── final.py
├── final_sentence/
│   ├── __init__.py
│   ├── app.py              # 核心 Controller：初始化、遊戲主循環與核心業務邏輯
│   ├── view.py             # View 層：Tkinter 全螢幕畫布動態 HUD 渲染與轉場動畫
│   ├── models.py           # Model 層：基於 Dataclass 的全域狀態機封裝
│   ├── texts.py            # 遊戲文本庫、多人在線規則以及文本格式化
│   ├── paths.py            # 靜態資源（音效、圖片）路徑解析器
│   ├── network.py          # 網路層：Socket JSON-Stream 通訊與本機 IP 探測
│   ├── audio.py            # 音效層：基於 Pygame.mixer 的多通道音效控制器
│   ├── image_tools.py      # 影像處理：PIL (Pillow) 動態渲染與角度旋轉特效
│   ├── missions.py         # 任務系統：任務讀寫、進度判定與 JSON 持久化
│   └── leaderboard.py      # 排行榜系統：戰績存檔與多維度排序演算法
├── assets/
│   ├── images/             # 桌、椅、螢幕、時鐘、名牌、血跡等圖檔 (.png)
│   └── audio/              # 節拍、開槍、空槍、錯誤、滾動與背景 BGM (.mp3 / .wav)
└── data/
    ├── missions.json       # 任務進度存檔 (自動生成)
    └── leaderboard.json    # 本地歷史紀錄 (自動生成)
```

### 🧩 模組職責詳解

* **`app.py` (Orchestrator/Controller)**
  連接各組件的核心。管理打字事件監聽 (`<Key>`)、節奏計時、俄羅斯輪盤動畫控制、多人連線的非同步事件隊列輪詢 (`poll_network_events`)，以及主選單與結算畫面的順滑淡入淡出。
* **`view.py` (Dynamic Canvas Renderer)**
  利用 Tkinter 進行像素級的全螢幕 Canvas 排版。包含：
  * Tilted Clock (傾斜鬧鐘) 與 Rank Plate (歪斜名牌) 的特殊渲染。
  * 六孔彈巢 (Revolver HUD) 的動態高亮。
  * 對手進度條 (Opponent Progress Bar) 在多人對戰時的動態刻畫。
* **`models.py` (Data Models)**
  使用 Python `dataclasses` 嚴格定義遊戲狀態，包括 `GameState`、`MenuState`、`MultiplayerState`、`StatsState`、`LayoutState` 等，防止變數命名混亂並提升編譯/直譯期靜態檢查。
* **`network.py` (TCP Socket Lobby)**
  提供純 Python 打造的 LAN Socket 通訊。利用 `send_json` 發送一行 JSON 字串，並在背景執行緒中非同步監聽 `read_json_lines`，實現無卡頓的連線體驗。
* **`leaderboard.py` (Sorting Weights Algorithm)**
  自訂本地排行榜多維度權重排序演算法。排名權重順序：
  $$\text{Result (Won/Lost)} \rightarrow \text{Completion Rate} \rightarrow \text{Average WPM} \rightarrow \text{Mistakes (Ascending)} \rightarrow \text{Max WPM}$$
* **`missions.py` (Achievement System)**
  定義了五大成就指標（首通、首勝、Combo 達 20、準確度達 80%、輪盤生存 3 次），並透過本地 `missions.json` 自動讀寫追蹤。

---

## 🚀 快速開始 (Installation & Setup)

### 1. 系統需求
本專案依賴 `Pillow` 作為 GUI 圖片處理元件，以及 `Pygame` 的混音模組來輸出高還原度的槍擊與打字音效。
* Python 3.8+

### 2. 安裝依賴套件
```bash
pip install Pillow pygame
```

### 4. 執行遊戲
在專案根目錄，透過 Python 模組方式啟動主程式：
```bash
python -m final.py
```

---

## 💻 網路多人連線配置 (LAN Multiplayer)

本遊戲採用 **點對點 LAN 連線模型**。無需額外設定伺服器，一位玩家擔任主機 (Host)，其餘玩家輸入主機 IP 即可加入：

```text
               ┌───────────────┐
               │  Host Player  │ (Port 50505)
               └───────┬───────┘
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
┌────────────────┐           ┌────────────────┐
│ Client Player  │           │ Client Player  │
└────────────────┘           └────────────────┘
```

1. **主機端 (Host)**：
   * 進入主選單 -> 點擊 `Multiplayer` -> `Host Game`。
   * 輸入你的玩家名稱，畫面將顯示本機 IP 位址（例如 `Hosting on 192.168.1.105:50505`）。
   * 等待其他玩家加入後，點擊 `Start Match`。
2. **用戶端 (Client)**：
   * 點擊 `Multiplayer` -> `Join Game`。
   * 輸入玩家名稱，並輸入主機提供的 IP 位址（例如 `192.168.1.105`）。
   * 連線成功後將進入等待室，主機開啟遊戲時會自動同步載入。

---

## ⚙️ 二次開發指南 (Developer Guide)

### 如何擴充自訂文本庫？
你可以在 `app/texts.py` 中的 `PREDEFINED_TEXTS` 清單中自由添加或編輯文本。
系統會自動在加載時處理縮排格式化：

```python
# app/texts.py
PREDEFINED_TEXTS = [
    # 在這裡新增你想要的段落
    "This is a custom typing paragraph.\nTry to type this as fast as possible.\nAnd survive the trial!\n",
]
```

### 任務定義結構
如果你想自訂新任務，可以直接修改 `app/missions.py` 中的 `MISSION_DEFS`：
```python
{
    "id": "new_challenge",
    "title": "完美主義者",
    "description": "單場打字錯誤次數小於 2 次通關。",
    "target": 1,
    "metric": "perfect_runs",
}
```

---

## 📜 授權條款 (License)

本專案基於 **MIT License** 授權開源。歡迎任何形式的 Fork、修改與教學使用。

---

### ⚠️ 溫馨提醒
* **全螢幕限制**：本遊戲啟動後會預設開啟全螢幕模式，您可以隨時在遊戲中按下 `Esc` 鍵開啟選單返回桌面，或者點擊畫面任何位置安全退出。
* **音樂設定**：遊戲音量預設為 100%。如果覺得音效過於震撼，可以點擊 `Options` 對背景音樂 (Music) 與音效 (Sound) 進行無段式拖曳調整。
