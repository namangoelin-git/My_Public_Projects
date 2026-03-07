# 🌞 Solar Plant Annual Overview

*Note: I’ve shared only the dashboard layout and visualization approach; the core calculation logic is kept private.*

**© Developed by Naman Goel** | Data Analyst 

## 📸 Dashboard Preview

<img width="1244" height="1006" alt="image" src="https://github.com/user-attachments/assets/978405d0-4e78-4f86-920b-edd96e480419" />

---

## Sample Data
<img width="1155" height="991" alt="image" src="https://github.com/user-attachments/assets/45b55de5-1f0c-4f9d-a536-06b4e4a899b3" />

---

## 📌 Project Overview

A Python-based data analytics dashboard that processes and visualizes a full year of solar energy production data. The dashboard transforms raw energy meter readings into meaningful KPIs and charts, providing a clear overview of solar plant performance.

---

## 🎯 Objective

To analyze annual solar energy production data and present it in a clean, professional dashboard that highlights key performance metrics, monthly trends, and daily peaks.

---

## 📊 Dashboard Features

### KPI Cards
| KPI | Description |
|-----|-------------|
| **Total Production** | Total yearly energy generated (kWh) |
| **Best Production Month** | Month with the highest energy output |
| **Best Production Day** | Single day with the highest energy output |

### Charts
- **Yearly Production Chart** — Line chart showing cumulative energy over the year
- **Lowest/Highest Month Comparison** — Bar chart comparing best vs worst month
- **Monthly Production Breakdown** — Bar chart showing energy produced each month with labels

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python** | Core programming language |
| **Pandas** | Data loading, cleaning & aggregation |
| **Matplotlib** | Dashboard layout & data visualization |
| **Calendar** | Converting month numbers to month names |

---

## 🔄 Data Processing Steps

1. **Load Data** — Read CSV with Date and Energy meter readings
2. **Calculate Delta Energy** — Compute daily/monthly production from cumulative readings
3. **Aggregate** — Group by month and day to compute totals
4. **Extract KPIs** — Identify yearly total, best month, best day
5. **Visualize** — Build multi-panel dashboard using `subplot2grid`

---

## 💡 Key Learnings

- Working with **time-series energy data** in Pandas
- Building **multi-panel dashboards** using `subplot2grid` with custom `colspan`
- Designing **KPI cards** with custom backgrounds, borders, and text styling
- Handling **cumulative vs delta energy** calculations
- Creating **annotated bar charts** with value labels

---

## 🚀 Future Improvements

- [ ] Add daily production chart
- [ ] Include weather data correlation
- [ ] Add energy forecasting using ML
- [ ] Convert to interactive dashboard using Plotly or Power BI
- [ ] Automate report generation for multiple years



