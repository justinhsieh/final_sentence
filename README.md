# Define the Markdown content for README.md in Traditional Chinese (Taiwanese localized).
readme_content = """# Final Sentence (終極判決) ⚖️💀

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![GUI Framework](https://img.shields.io/badge/GUI-Tkinter-lightgrey.svg)](https://docs.python.org/3/library/tkinter.html)
[![Audio Library](https://img.shields.io/badge/Audio-Pygame.mixer-red.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Final Sentence** 是一款將「極限打字」與「俄羅斯輪盤 (Russian Roulette)」完美融合的高壓生存打字遊戲。
在這裡，打字不只是精準度的考驗，更是一場關乎生死的賭局。在每關 240 秒的緊迫倒數與無情敲擊聲中，任何一次手滑、錯字都可能將你推向左輪手槍的槍口。

本專案採用類似 **MVC (Model-View-Controller) 的架構設計**，並原生支援 **區域網路 (LAN) 多人即時連線對戰**、**持久化本地任務系統**與**排行榜系統**。

---

## 🎮 核心遊戲機制 (Gameplay Mechanics)

1. **五重極限審判**：
   * 玩家必須在單場遊戲中，連續正確輸入 **5 篇預設或自訂文本**。
   * 每篇文本有獨立的 **240 秒倒數計時**。若計時歸零，無情大衣男子會直接開槍，挑戰失敗。
2. **三擊輪盤規則 (Three-Strike Russian Roulette)**：
   * 遊戲中允許累積 **3 次打字失誤**（Strikes）。
   * 當失誤滿 3 次時，介面會被凍結，隨即觸發**俄羅斯輪盤抽獎**：
     * 系統隨機裝填一顆子彈並瘋狂旋轉彈巢。
     * 轉動停止後扣動扳機。
     * **中彈** 💥：大衣男子扣動扳機，遊戲直接結束 (YOU ARE DEAD!!)。
     * **倖存** 🔒：發出清脆的「喀噠」空槍聲。玩家失誤次數歸零，但文本會**強制回滾 (Reset) 至當前行開頭**，且下一次觸發輪盤時，中彈機率將隨裝填子彈數增加而急遽上升！
3. **即時連線淘汰賽**：
   * 支援私人區域網路 (LAN) 房。所有玩家在同一時間輸入相同的 5 篇文本。
   * 第一個無失誤通關所有文本的玩家獲勝。若其他玩家皆中彈身亡，最後的倖存者自動奪冠！

---

## 🛠️ 系統架構與模組設計 (Architecture & Modules)

本專案將**狀態管理 (Model)**、**視覺渲染 (View)** 與 **業務邏輯控制 (Controller)** 徹底分離，架構極其清晰，便於二次開發與擴充。

### 📂 專案目錄結構
