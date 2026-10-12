# 🍕 Comprehensive End-to-End Pizza Sales Analytics Project

## Executive Summary & Project Overview

This project delivers a complete, multi-platform data analytics solution for a comprehensive pizza restaurant dataset. The analytical pipeline spans raw data ingestion, advanced data cleaning in Excel (Power Query), relational database modeling and querying in MySQL, exploratory data analysis (EDA) and visualization using Python (Matplotlib & Seaborn), Excel PivotCharts, enterprise-grade dashboard development in Power BI and Tableau, and automated executive reporting via OpenPyXL.

### Key Performance Indicators (KPIs)
- **Total Revenue:** $817,860.05
- **Total Orders:** 21,350
- **Total Pizzas Sold:** 49,574
- **Average Order Value (AOV):** $38.31
- **Average Pizzas per Order:** 2.32

## 🚀 Project Phases & Architecture

### Phase 1: Data Preparation & Transformation (Excel & Power Query)

Raw transactional data was cleaned and structured to ensure data integrity and analytical readiness:

1. **File Ingestion:** Opened `pizza_sales_data.xlsx` in Excel.
2. **Column Removal:** Removed the redundant `pizza_ingredients` column. 
3. **Data Cleaning (`pizza_size`):** Standardized size abbreviations (`S` → `Small`, `M` → `Medium`, `L` → `Large`, `XL` → `X-Large`, `XXL` → `XX-Large`).
4. **Calculated Date & Time Features:** Extracted `order_weeknum`, `order_day` (e.g., `Sun`, `Mon`), `order_month` (e.g., `Jan`, `Feb`), and formatted `order_hour` (e.g., `11 AM`, `12 PM`).
5. **Unique Orders Flag:** Added `unique_orders` column.
6. **Export:** Saved final output as `pizza_sales_transformed_data.xlsx`.

### Phase 2: Database Management & SQL Analysis (MySQL & Python)

- **Schema Design & Creation:** Built relational database schema (`pizza_db`) with optimized data types and constraints.
- **Data Ingestion:** Automated loading of transformed data into MySQL via Python scripts. 
- **Analytical Queries:** Computed total revenue, AOV, hourly/daily trends, category/size percentage contributions, and top/bottom rankings.

### Phase 3: Exploratory Data Analysis & Visualization (Excel PivotCharts)

Constructed structured analytical sheets and interactive PivotCharts:

- `KPI_Metrics` Sheet: Total Revenue, Units Sold, Orders, AOV, and Pizzas per Order.
- `Trends_for_Total_Orders` Sheet: Daily bar charts, hourly line charts, and monthly trend visualizations.
- `%_of_Sales` Sheet: Category donut charts and size pie charts.
- `best_&_worst_sellers` Sheet: Top and bottom 5 sellers by volume and revenue.
- Dashboard Sheet: Integrated executive summary view.

### Phase 4: Advanced Business Intelligence & Dashboards (Power BI)

Loaded transformed data into Power BI to build a robust semantic model with DAX measures and calculated calendar tables:

- **Dashboard 1 (HOME):** KPI scorecards, daily/monthly trend visuals, category/size breakdown, and interactive slicers.
- **Dashboard 2 (BEST & WORST SELLERS):** Horizontal bar graphs detailing top and bottom 5 sellers by revenue and quantity.

### Phase 5: Enterprise Analytics & Dashboarding (Tableau)

Built two comprehensive Tableau analytical dashboards:

- **Pizza Sales Dashboard (HOME):** Visualized hourly/daily heatmaps, monthly trends, category shares, and size preferences.
- **Best & Worst Sellers Dashboard:** Highlighted revenue leaders (Thai Chicken), volume champions (Classic Deluxe), and low performers (Brie Carre).

### Phase 6: Python EDA & Matplotlib/Seaborn Visualization (`.ipynb`)

Utilized Jupyter Notebooks with `pandas`, `numpy`, `matplotlib`, and `seaborn` to execute programmatic data aggregations, heatmaps, and publication-quality plots. Key insights led to strategic recommendations regarding menu rationalization, combo bundling, and inventory optimization.

### Phase 7: Automated Excel Executive Report Generation (Python & OpenPyXL)

Developed a custom Python automation script (`generate_pizza_report.py`) utilizing `pandas` and `openpyxl` to programmatically ingest data, apply professional formatting, inject native formulas, adjust column widths, and generate `pizza_sales_executive_report.xlsx`.

## 📁 Repository Structure

```Plaintext
├── 01_Raw_data/
│   └── pizza_sales_data.xlsx               # Raw transactional dataset
├── 02_Transformed_data/
│   └── pizza_sales_transformed_data.xlsx     # Power Query cleaned dataset
├── 03_SQL/
│   ├── 03.01_Create_SQL_Schema.sql           # Database schema
│   ├── 03.02_Load_Data_to_MySQL
│   │   ├── .env.example                      # SQL Credentials
│   │   ├── utils.py                          # Utility script
│   │   └── main.py                           # Main script to load excel file to SQL
│   ├── 03.03_SQL_Queries_Pizza_Sales.sql     # Analytical Queries
│   ├── 03.04_SQL_Pizza_Sales_Report.docx     # Report of Queries
│   └── 03.05_SQL_Pizza_Sales_Report.pdf      # PDF Report
├── 04_Excel/
│   └── Pizza_sales_pivot_chart_dashboard.xlsx # Excel Dashboard
├── 05_Power_BI/
│   └── Power_BI_dashboards.pbix              # Power BI interactive workbook
├── 06_Tableau/
│   └── Tableau_Dashboard.twb                 # Tableau interactive workbook
├── 07_Matplotlib/
│   ├── matplotlib_visualization.ipynb        # Python EDA & Matplotlib plots
│   └── matplotlib_visualization.pdf          # PDF Report
├── 08_Python_report_automation/
│   ├── generate_pizza_report.py              # OpenPyXL automated Excel report script
│   └── pizza_sales_executive_report.xlsx     # Output file
└── README.md                                 # Project documentation
```

## 🛠️ Technologies Used

- **Python** (Pandas, NumPy, Matplotlib, Seaborn, OpenPyXL) 
- **SQL / MySQL** (Database design, Window functions, CTEs)
- **Microsoft Excel** (Power Query, Pivot Tables, PivotCharts)
- **Power BI** (DAX modeling, Interactive dashboards)
- **Tableau** (Enterprise visual analytics)
- **Markdown** (Documentation)

## 💡 Key Insights & Strategic Recommendations

1. **Peak Operating Windows:** Orders peak sharply during Lunch (12:00 PM – 2:00 PM) and Dinner (4:00 PM – 8:00 PM), with Thursday and Friday recording highest weekly volumes.
    - _Recommendation:_ Align kitchen staffing and delivery schedules around peak windows to minimize fulfillment latency.

2. **Product Performance:** Premium chicken pizzas (e.g., Thai Chicken) drive high revenue, while Classic Deluxe acts as the primary volume driver. Niche items like Brie Carre show very low turnover.
    - _Recommendation:_ Feature top heroes on app banners and menus while considering the rationalization of ultra-low-demand items (<1% share) to reduce waste.

3. **AOV Enhancement:** Strategic bundle offers and promotional cross-selling can effectively lift Average Order Value.

## 👤 Author

**Name:** Animesh Sanghi
**Profession:** Google Certified Data Analyst
**LinkedIn:** [linkedin.com/in/animeshsanghi-da](https://www.linkedin.com/in/animeshsanghi-da/)
**GitHub:** [github.com/animeshsanghi-da](https://github.com/animeshsanghi-da)
**Email:** animeshsanghi.da@gmail.com

## 📜 License

This project is open-source and free to use for educational and professional demonstration purposes.