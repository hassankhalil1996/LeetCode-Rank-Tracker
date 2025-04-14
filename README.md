# 🧠 LeetCode Rank Tracker

This project automatically scrapes and logs your **LeetCode global ranking** daily using Python and Task Scheduler (Windows only), then visualizes the ranking trend over time.

---

## 🚀 Features

- ✅ Automatically scrapes your LeetCode rank once a day
- ✅ Logs rank into a CSV file with timestamps
- ✅ Visualizes your progress using a clean line chart

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `fetch_rank.py` | Uses Selenium to scrape your LeetCode rank and log it to `rank_history.csv` |
| `automated_task_sched.py` | Registers a Windows Task Scheduler job to run `fetch_rank.py` daily |
| `VisualizeChart.py` | Plots your LeetCode rank history using Matplotlib |

---

## 🛠 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/LeetCode-Rank-Tracker.git
cd LeetCode-Rank-Tracker
```

### 2. Run setup.bat

### 3. Run view_rank_chart.bat to show your rank 


---
# 📌 Notes
    - Windows only (uses COM automation via win32com)

    - Make sure Python is in your PATH

    - You must customize the username in fetch_rank.py

    - You need to be logged in to your LeetCode profile
---


# ✨ Demo
- (Insert a chart screenshot or GIF if you want)
---


# 📜 License
- MIT License
---