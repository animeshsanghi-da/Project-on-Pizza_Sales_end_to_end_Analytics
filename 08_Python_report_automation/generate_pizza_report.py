import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
import pandas as pd


def load_data(file_path):
    """Loads the dataset from Excel."""
    return pd.read_excel(file_path)


def compute_metrics(df):
    """Computes all summary dataframes and metrics."""
    total_revenue = df["total_price"].sum()
    total_orders = df['unique_order'].sum()
    total_pizzas_sold = df["quantity"].sum()

    # Sheet 1
    kpi_df = pd.DataFrame(
        {
            "Metric": [
                "Total Revenue",
                "Total Orders",
                "Total Pizzas Sold",
                "Average Order Value (AOV)",
                "Average Pizzas per Order",
            ],
            "Value": [
                total_revenue,
                total_orders,
                total_pizzas_sold,
                total_revenue / total_orders,
                total_pizzas_sold / total_orders,
            ],
        }
    )

    # Sheet 2
    day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    daily_trend_df = df.groupby(df['order_day']).agg(
        Total_Orders=('unique_order', 'sum'),
        Total_Revenue=('total_price', 'sum')
    ).reindex(day_order).reset_index()

    hourly_trend_df = df.groupby(df['order_hour']).agg(
        Total_Orders=('unique_order', 'sum'),
        Total_Revenue=('total_price', 'sum')
    ).reset_index()

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_trend_df = df.groupby(df['order_month']).agg(
        Total_Orders=('unique_order', 'sum'),
        Total_Revenue=('total_price', 'sum')
    ).reindex(month_order).reset_index()


    # Sheet 3
    per_sales_by_category_df = (
        df.groupby("pizza_category")
        .agg(
            Total_Revenue=("total_price", "sum"),
            Total_Quantity=("quantity", "sum"),
        )
        .reset_index()
    )
    per_sales_by_category_df["Revenue_Share_%"] = (per_sales_by_category_df["Total_Revenue"] / total_revenue)

    per_sales_by_size_df = (
        df.groupby("pizza_size")
        .agg(
            Total_Revenue=("total_price", "sum"),
            Total_Quantity=("quantity", "sum"),
        )
        .reset_index()
    )
    per_sales_by_size_df["Revenue_Share_%"] = (per_sales_by_size_df["Total_Revenue"] / total_revenue)
    
    
    # Sheet 4
    top_sellers_by_qty = (
        df.groupby("pizza_name")
        .agg(
            Total_Quantity=("quantity", "sum"),
        )
        .reset_index()
        .sort_values(by="Total_Quantity", ascending=False)
        .head(5)
    )

    bottom_sellers_by_qty = (
        df.groupby("pizza_name")
        .agg(
            Total_Quantity=("quantity", "sum"),
        )
        .reset_index()
        .sort_values(by="Total_Quantity", ascending=True)
        .head(5)
    )

    top_sellers_by_revenue = (
        df.groupby("pizza_name")
        .agg(
            Total_Revenue=("total_price", "sum"),
        )
        .reset_index()
        .sort_values(by="Total_Revenue", ascending=False)
        .head(5)
    )

    bottom_sellers_by_revenue = (
        df.groupby("pizza_name")
        .agg(
            Total_Revenue=("total_price", "sum"),
        )
        .reset_index()
        .sort_values(by="Total_Revenue", ascending=True)
        .head(5)
    )

    return kpi_df, daily_trend_df, hourly_trend_df, monthly_trend_df, per_sales_by_category_df, per_sales_by_size_df, top_sellers_by_qty, bottom_sellers_by_qty, top_sellers_by_revenue, bottom_sellers_by_revenue


def write_table_to_sheet(ws, start_row, title, df_data):
    """Writes a styled table onto a worksheet."""
    ws.cell(row=start_row - 1, column=1, value=title).font = Font(
        name="Calibri", size=14, bold=True, color="1F4E78"
    )

    header_fill = PatternFill(
        start_color="1F4E78", end_color="1F4E78", fill_type="solid"
    )
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    cell_border = Border(
        left=Side(style="thin", color="000000"),
        right=Side(style="thin", color="000000"),
        top=Side(style="thin", color="000000"),
        bottom=Side(style="thin", color="000000"),
    )

    # Write headers
    for col_idx, col_name in enumerate(df_data.columns, 1):
        cell = ws.cell(row=start_row, column=col_idx, value=col_name)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = cell_border

    # Write data rows
    for r_idx, row_vals in enumerate(df_data.values, start_row + 1):
        for c_idx, val in enumerate(row_vals, 1):
            cell = ws.cell(row=r_idx, column=c_idx, value=val)
            cell.font = Font(name="Calibri", size=11)
            cell.border = cell_border

            # Simple formatting logic
            if isinstance(val, (int, float)):
                col_name = str(df_data.columns[c_idx - 1])
                row_label = (
                    str(row_vals[0]) if "Metric" in df_data.columns else ""
                )

                if "%" in col_name:
                    cell.number_format = "0.0%"
                elif (
                    "Revenue" in col_name
                    or "Revenue" in row_label
                    or "AOV" in row_label
                ):
                    cell.number_format = "$#,##0.00"
                elif "Orders" in row_label or "Sold" in row_label:
                    cell.number_format = "#,##0"
                elif "Order" in row_label or "Per" in row_label:
                    cell.number_format = "0.00"
                else:
                    cell.number_format = "#,##0"

                cell.alignment = Alignment(horizontal="right", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center")

    # Auto-fit columns
    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 15)


def generate_report(output_file):
    print("1. Loading data...")
    df = load_data("../02_Transformed_data/pizza_sales_transformed_data.xlsx")

    print("2. Computing metrics...")
    kpi_df, daily_trend_df, hourly_trend_df, monthly_trend_df, per_sales_by_category_df, per_sales_by_size_df, top_sellers_by_qty, bottom_sellers_by_qty, top_sellers_by_revenue, bottom_sellers_by_revenue = compute_metrics(df)

    print("3. Building Excel workbook...")
    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # Remove default sheet

    # Sheet 1: KPI Metrics
    ws1 = wb.create_sheet(title="KPI Metrics")
    ws1.views.sheetView[0].showGridLines = True
    write_table_to_sheet(ws1, start_row=2, title="Executive KPIs", df_data=kpi_df)

    # Sheet 2: Trends for Total Orders
    ws2 = wb.create_sheet(title="Trends for Total Orders")
    ws2.views.sheetView[0].showGridLines = True
    write_table_to_sheet(ws2, start_row=2, title="Daily Trend of Total Orders", df_data=daily_trend_df)
    write_table_to_sheet(ws2, start_row=len(daily_trend_df) + 6, title="Hourly Trend of Total Orders", df_data=hourly_trend_df)
    write_table_to_sheet(ws2, start_row=len(daily_trend_df) + len(hourly_trend_df) + 10, title="Monthly Trend of Total Orders", df_data=monthly_trend_df)

    # Sheet 3: Percentage of Sales
    ws3 = wb.create_sheet(title="Percentage of Sales")
    ws3.views.sheetView[0].showGridLines = True
    write_table_to_sheet(ws3, start_row=2, title="Percentage Sales by Pizza Category", df_data=per_sales_by_category_df)
    write_table_to_sheet(ws3, start_row=len(per_sales_by_category_df) + 6, title="Percentage Sales by Pizza Size", df_data=per_sales_by_size_df)

    # Sheet 4: Best and Worst Sellers
    ws4 = wb.create_sheet(title="Categories & Top Sellers")
    ws4.views.sheetView[0].showGridLines = True
    write_table_to_sheet(ws4, start_row=2, title="Top 5 Sellers by Total Pizzas Sold", df_data=top_sellers_by_qty)
    write_table_to_sheet(ws4, start_row=len(top_sellers_by_qty) + 6, title="Bottom 5 Sellers by Total Pizzas Sold", df_data=bottom_sellers_by_qty)
    write_table_to_sheet(ws4, start_row=len(top_sellers_by_qty) + len(bottom_sellers_by_qty) + 10, title="Top 5 Sellers by Total Revenue", df_data=top_sellers_by_revenue)
    write_table_to_sheet(ws4, start_row=len(top_sellers_by_qty) + len(bottom_sellers_by_qty) + len(top_sellers_by_revenue) + 14, title="Bottom 5 Sellers by Total Revenue", df_data=bottom_sellers_by_revenue)

    wb.save(output_file)
    print(f"Report saved successfully as '{output_file}'!")


if __name__ == "__main__":
    output_file = "pizza_sales_executive_report.xlsx"
    generate_report(output_file)