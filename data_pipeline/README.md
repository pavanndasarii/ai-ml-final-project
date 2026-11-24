# Books Data Pipeline

## Overview

This project builds an end-to-end data pipeline using Python, web scraping, Pandas, and SQLite.

The main objective is to collect book information from the [Books to Scrape](https://books.toscrape.com/) website, clean and transform the collected data, store it in a relational database, and perform SQL-based analysis.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- NumPy
- SQLite
- SQL

## Pipeline Workflow

1. Scrape book information from the first five catalogue pages.
2. Collect book titles, prices, star ratings, availability, and categories.
3. Explore the collected data and check for missing values and duplicates.
4. Clean prices by removing currency symbols and converting them into floating-point values.
5. Convert text-based ratings into integers from 1 to 5.
6. Convert availability into Boolean values.
7. Handle invalid records and correct category labels.
8. Convert GBP prices into INR using a fixed conversion rate.
9. Store the cleaned data in two related SQLite tables.
10. Perform SQL queries and compare SQL JOIN results with Pandas merge results.
11. Validate the final dataset and database relationships.

## Data Cleaning and Quality Decisions

- Removed unwanted characters such as `Â` and `£` from book prices.
- Used `errors='coerce'` to handle invalid numeric prices.
- Converted text-based star ratings into numerical values.
- Handled unexpected rating and availability values during cleaning.
- Checked for missing values and duplicate records before database insertion.
- Chose to drop invalid records instead of using median imputation to avoid introducing artificial prices or ratings.
- Replaced the invalid category label `Add a comment` with `Unknown` to preserve the affected books.
- Validated that the cleaned dataset meets the minimum requirement of 60 books across at least three categories.

## Currency Conversion

The project uses the following fixed conversion rate:

**1 GBP = 105.50 INR**

This is a project-defined constant and not a live or historical exchange rate. No external currency API is used.

The converted INR prices are rounded to two decimal places.

## Database Design

The SQLite database consists of two normalized tables:

### Categories

| Column | Data Type |
|---|---|
| category_id | INTEGER (Primary Key) |
| category_name | TEXT (Unique) |

### Books

| Column | Data Type |
|---|---|
| book_id | INTEGER (Primary Key) |
| title | TEXT |
| price_gbp | REAL |
| price_inr | REAL |
| rating | INTEGER |
| in_stock | INTEGER |
| category_id | INTEGER (Foreign Key) |

The two tables are connected through `category_id`. This avoids unnecessary repetition of category names and maintains referential integrity.

Boolean availability values are stored as `1` for True and `0` for False in SQLite.

## SQL Analysis

The project includes nine SQL queries covering:

- Filtering books using SELECT and WHERE.
- Sorting books using ORDER BY.
- Retrieving highly rated books using LIMIT.
- Finding unique ratings using DISTINCT.
- Filtering books within a price range using BETWEEN.
- Joining books with their respective categories.
- Counting books by category.
- Calculating average, minimum, and maximum book prices.
- Counting total books and distinct categories.

The query results are retrieved using `pd.read_sql()`.

The SQL JOIN result is also reproduced independently using `pd.merge()` on in-memory DataFrames. Both results are displayed side by side and checked for equality.

## Validation Results

| Check | Expected Result |
|---|---:|
| Books collected | 100 |
| Catalogue pages scraped | 5 |
| Unique categories | 29 |
| Duplicate records after cleaning | 0 |
| Missing values after cleaning | 0 |
| Books with corrected category | 5 |
| SQL queries | 9 |
| SQL JOIN and Pandas merge | Match |
| Foreign key errors | 0 |

Final validation checks ensure that record counts and category counts match between the cleaned DataFrame and SQLite database. Rating ranges, stock values, and foreign key relationships are also checked.

Successful execution of the final validation checks produces:

`All final checks passed.`

## Generated Output Files

The notebook generates the following files during execution:

- `books.db` — SQLite database containing the cleaned book records and categories.
- `sql_queries.sql` — SQL statements used for analysis.
- `query_outputs/` — SQL query results and Pandas merge output saved as CSV files.

## How to Run

1. Install the required Python libraries:

   `pip install requests beautifulsoup4 pandas numpy`

2. Open `01_data_pipeline.ipynb` in Jupyter Notebook or Google Colab.
3. Run all cells in sequence.
4. Check the generated database, SQL query outputs, and final validation results.

An internet connection is required to scrape data from the website.

## Conclusion

Through this project, I gained practical experience in web scraping, data cleaning, data transformation, relational database design, and SQL analysis.

The final outcome is a reusable, structured, and validated book database that can be used for further analysis without scraping the website again. This project helped me understand how a complete ETL data pipeline works, from collecting raw data to storing and analyzing processed information.
