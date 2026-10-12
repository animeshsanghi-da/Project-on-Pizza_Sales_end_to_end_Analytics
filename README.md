# 🍕 Comprehensive End-to-End Pizza Sales Analytics Project

[![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://www.microsoft.com/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://www.tableau.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)


[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/SeabStr-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![OpenPyXL](https://img.shields.io/badge/OpenPyXL-217346?style=for-the-badge&logo=python&logoColor=white)](https://openpyxl.readthedocs.io/)

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

![Power Query Transformation](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/1.0_power_query.png)

### Phase 2: Database Management & SQL Analysis (MySQL & Python)

- **Schema Design & Creation:** Built relational database schema (`pizza_db`) with optimized data types and constraints.
- **Data Ingestion:** Automated loading of transformed data into MySQL via Python scripts. 
- **Analytical Queries:** Computed total revenue, AOV, hourly/daily trends, category/size percentage contributions, and top/bottom rankings.

![MySQL Query](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/2.0_SQL.png)

### Phase 3: Exploratory Data Analysis & Visualization (Excel PivotCharts)

Constructed structured analytical sheets and interactive PivotCharts:

- `KPI_Metrics` Sheet: Total Revenue, Units Sold, Orders, AOV, and Pizzas per Order.
- `Trends_for_Total_Orders` Sheet: Daily bar charts, hourly line charts, and monthly trend visualizations.
- `%_of_Sales` Sheet: Category donut charts and size pie charts.
- `best_&_worst_sellers` Sheet: Top and bottom 5 sellers by volume and revenue.
- Dashboard Sheet: Integrated executive summary view.

![Excel Dashboard](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/3.0_Excel_PivotCharts.png)

### Phase 4: Advanced Business Intelligence & Dashboards (Power BI)

Loaded transformed data into Power BI to build a robust semantic model with DAX measures and calculated calendar tables:

- **Dashboard 1 (HOME):** KPI scorecards, daily/monthly trend visuals, category/size breakdown, and interactive slicers.
- **Dashboard 2 (BEST & WORST SELLERS):** Horizontal bar graphs detailing top and bottom 5 sellers by revenue and quantity.

![Power BI 1](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/4.1_Power_BI.png)
![Power BI 2](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/4.2_Power_BI.png)

### Phase 5: Enterprise Analytics & Dashboarding (Tableau)

Built two comprehensive Tableau analytical dashboards:

- **Pizza Sales Dashboard (HOME):** Visualized hourly/daily heatmaps, monthly trends, category shares, and size preferences.
- **Best & Worst Sellers Dashboard:** Highlighted revenue leaders (Thai Chicken), volume champions (Classic Deluxe), and low performers (Brie Carre).

![Tableau 1](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/5.1_Tableau.png)
![Tableau 2](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/5.2_Tableau.png)

### Phase 6: Python EDA & Matplotlib/Seaborn Visualization (`.ipynb`)

Utilized Jupyter Notebooks with `pandas`, `numpy`, `matplotlib`, and `seaborn` to execute programmatic data aggregations, heatmaps, and publication-quality plots. Key insights led to strategic recommendations regarding menu rationalization, combo bundling, and inventory optimization.

![plt 1](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/6.1_matplotlib.png)
![plt 2](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/6.2_matplotlib.png)
![plt 3](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/6.3_matplotlib.png)

### Phase 7: Automated Excel Executive Report Generation (Python & OpenPyXL)

Developed a custom Python automation script (`generate_pizza_report.py`) utilizing `pandas` and `openpyxl` to programmatically ingest data, apply professional formatting, inject native formulas, adjust column widths, and generate `pizza_sales_executive_report.xlsx`.

![python automation](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/7.0_python_automation.png)

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

![insights](https://raw.githubusercontent.com/animeshsanghi-da/Project-on-Pizza_Sales_end_to_end_Analytics/main/Images/dashboards/9.9_insights_recommendations.png)

## 👤 Author

**Name:** Animesh Sanghi  
**Profession:** Google Certified Data Analyst  
**LinkedIn:** [linkedin.com/in/animeshsanghi-da](https://www.linkedin.com/in/animeshsanghi-da/)  
**GitHub:** [github.com/animeshsanghi-da](https://github.com/animeshsanghi-da)  
**Email:** animeshsanghi.da@gmail.com

## 📜 License

This project is open-source and free to use for educational and professional demonstration purposes.
