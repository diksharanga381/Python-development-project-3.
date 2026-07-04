sales = [1200, 1500, 1800, 1300, 2000]


total_sales = sum(sales)
average_sales = total_sales / len(sales)
highest_sale = max(sales)
lowest_sale = min(sales)


report = f"""
SALES ANALYTICS REPORT
----------------------
Total Sales   : {total_sales}
Average Sales : {average_sales:.2f}
Highest Sale  : {highest_sale}
Lowest Sale   : {lowest_sale}
"""


with open("sales_report.txt", "w") as file:
    file.write(report)

print(report)
print("Report saved as sales_report.txt")