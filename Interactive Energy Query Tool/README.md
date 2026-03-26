# Interactive Energy Query Tool 

A lightweight, interactive command-line tool that lets you query solar energy production data by date range.

**© Developed by Naman Goel** | Data Analyst 

---

## 📌 Overview

This tool reads a CSV file containing hourly solar energy production records and allows you to quickly look up **total energy produced** within any custom date range — right from your terminal.

No machine learning. No APIs. Just fast, filtered results from your local data.

---

## 🛠️ Tech Stack

| Component     | Detail          |
|---------------|-----------------|
| Language      | Python 3.x      |
| Library       | Pandas           |
| Interface     | Command Line (CLI) |
| Data Format   | CSV (`Date`, `Energy`) |

---

## 📁 Expected CSV Format

Your input CSV file should have at least two columns:

| Date       | Energy |
|------------|--------|
| 2025-01-01 | 120.5  |
| 2025-01-02 | 98.3   |
| 2025-01-03 | 145.0  |

- **Date** — any format that `pandas.to_datetime()` can parse (e.g., `YYYY-MM-DD HH`)
- **Energy** — numeric values representing energy production (in kWh)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Pandas library

```bash
pip install pandas
```

### Installation

1. Clone or download this repository.
2. Place your CSV file at the path specified in the script, or update the path:

```python
df = pd.read_csv(r"your/path/to/data.csv")
```

3. Run the script:

```bash
Interactive Energy Query Tool.py
```

---

## 💡 Usage

Once launched, the tool displays a summary of the loaded data and prompts you for a date range.

```
╭────────────────────╮
│ ★ Data Overview ★ │
╰────────────────────╯
🔴 Total Rows: 8760
📅 Date range: 2025-01-01 00 to 2025-12-31 23
🔴 Total production: 247003 kWh

╭──────────────────────────────╮
│    Agent is asking.....      │
╰──────────────────────────────╯
❔ Enter the start and end dates to calculate total energy: 2025-01-01 00:00:00 to 2025-01-31 23:00:00

╭────────────────────╮
│    Agent Answer    │
╰────────────────────╯
Data Range Selected: 2025-01-01 00:00:00 to 2025-01-31 23:00:00
Selected Period Energy:  18177 kWh

╭──────────────────────────────╮
│    Agent is asking.....      │
╰──────────────────────────────╯
❔ Enter the start and end dates to calculate total energy:
```

### Input Format

```
YYYY-MM-DD HH to YYYY-MM-DD HH
```

**Examples:**
- `2025-01-01 00 to 2025-01-31 23`
- `2025-02-01 00 to 2025-04-31 10`

Type `quit` to exit the program.

---

## ⚙️ How It Works

1. **Loads** the CSV and parses the `Date` column into datetime objects.
2. **Prompts** the user for a date range in `YYYY-MM-DD HH to YYYY-MM-DD HH` format.
4. **Filters** the data using a boolean mask to find rows within the specified range.
5. **Calculates** and displays the total energy production for that period.

---

## ⚠️ Limitations

- Accepts only the strict `yyyy-mm-dd hh to yyyy-mm-dd hh` format.
- Does not support multiple CSV files or live data feeds.
- No graphical interface — terminal only.
- CSV must contain `Date` and `Energy` columns with those exact names.

---

## 📂 Project Structure

```
📦 Interactive Energy Query Tool
├── Interactive Energy Query Tool.py    # Main script
├── Test_Data.csv                       # Your energy production data
└── README.md                           # This file
```

---

## 🔮 Future Improvements

- Add support for natural language queries (e.g., "last week's total")
- Export filtered results to a new CSV
- Add data visualization with Matplotlib

---

## 📄 License

This project is for personal/educational use.

---

> Built with 🐍 Python & ☀️ Energy Data
