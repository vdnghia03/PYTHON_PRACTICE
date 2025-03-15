# **Aggregation definition**


Data aggregation is one of the most common tasks in data analytics. Data aggregation involves combining or summarizing multiple data points or observations into a single entity or a smaller set of entities. it enables us to transform raw data into more structured, manageable, and useful formats.

In the context of modern data orchestration, data aggregation is often used to summarize large datasets and make them more accessible for downstream analysis, reporting, visualization. This process involves grouping data by one or more variables and applying aggregate functions, such as mean, sum, count, or min/max, to calculate statistics or metrics for each group.

Data aggregation is commonly used in ETL pipelines to transform data from multiple sources into a single, consolidated dataset. For instance, in a marketing analytics pipeline, data from multiple sources, such as social media, email campaigns and website traffic, may be aggregated to generate a comprehensive view of marketing performance across channels.

Data aggregation is also a fundamental technique in data warehousing, where large volumes of data are processed and transformed to create a centralized repository of structured data. Data aggregation helps to reduce the size of these datasets by summarizing them into smaller, more manageable datasets that can be queried and analyzed more efficiently.

Overall, data aggregation is an important technique for modern data orchestration because it enables us to process, transform, and manage large volumes of data more effectively, leading to better insights and more informed decision-making.

# Data aggregation best practices


When running an aggregation, there are several best practices to keep in mind

![DataAggregation.png](Glossary_DE/image/DataAggregation.png)

# **Aggregation vs. Pre-aggregation**
---

Pre-aggregation involves creating summary tables or views that contain pre-computed aggregated values at different levels of granularity, such as daily, weekly, or monthly summaries. These pre-aggregated tables can be used to accelerate analytical queries by providing faster access to summarized data, as opposed to querying the raw, detailed data.

## **Example of data aggregation using Python**

```python
import pandas as pd

# create sample data
data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
	, 'Department': ['Marketing', 'Engineering', 'Marketing', 'Sales', 'Engineering']
	, 'Salary': [50000, 70000, 60000, 80000, 75000]
	, 'Bonus': [1000, 2000, 1500, 2500, 1800]
}
df = pd.DataFrame(data)

# group data by department and calculate mean salary and total bonus
agg_data = df.groupby('Department').agg({'Salary': 'mean', 'Bonus': 'sum'})

print(agg_data)
```

→ Result

```markdown
                 Salary  Bonus
Department
Engineering     72500.0   3800
Marketing       55000.0   2500
Sales           80000.0   2500
```

## **Example of data pre-aggregation using Python**

A gain, the process used in pre-aggregation is similar to that used in aggregation, but the end goal is different, optimizing for query performance and storage optimization. But here is a simple example of how we might pre-aggregate data, using Pandas.

```python
import pandas as pd

# create sample data
data = {
	'date': ['2023-06-01', '2023-06-01', '2023-06-01', '2023-06-01', '2023-06-02', '2023-06-02', '2023-06-03', '2023-06-03', '2023-06-03', '2023-06-03']
   , 'product': ['A','A', 'B', 'B', 'A', 'B', 'A', 'A', 'C', 'C']
   , 'sales': [100,300,200,50,150,250,180,120,60,60]
}
df = pd.DataFrame(data)

# Perform pre-aggregation
df_pre = df.groupby(['date', 'product']).sum().reset_index()

# Display the pre-aggregated DataFrame
print(f"Raw table:\n{df}")
print(f"Pre-aggregated table:\n{aggregated_df}")
```

→ Result
```markdown
Raw table:
         date product  sales
0  2023-06-01       A    100
1  2023-06-01       A    300
2  2023-06-01       B    200
3  2023-06-01       B     50
4  2023-06-02       A    150
5  2023-06-02       B    250
6  2023-06-03       A    180
7  2023-06-03       A    120
8  2023-06-03       C     60
9  2023-06-03       C     60
Pre-aggregated table:
         date product  sales
0  2023-06-01       A    400
1  2023-06-01       B    250
2  2023-06-02       A    150
3  2023-06-02       B    250
4  2023-06-03       A    300
5  2023-06-03       C    120
```

In this case, the pre-aggregated DataFrame provides a summary of the sales data by date and product, making it easier to perform queries and analysis on the aggregated data instead of the raw, detailed data. This simple example illustrates how, in many cases, you can optimize queries, reduce storage requirements, and also avoid downstream re-interpretation of how to calculate things like roll-ups.
