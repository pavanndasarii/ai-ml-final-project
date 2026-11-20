
# Books Data Pipeline

## Overview

This project builds an end-to-end data pipeline using Python, web scraping, Pandas, and SQLite.

It collects book information from the Books to Scrape website, cleans and transforms the data, stores it in a relational database, and performs SQL-based analysis.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- SQLite
- SQL

## Pipeline Workflow

1. Scraped book information from five website pages.
2. Collected 100 book records, including title, price, rating, availability, and category.
3. Cleaned prices by removing currency symbols and converting values into numeric format.
4. Converted text-based ratings into numerical values from 1 to 5.
5. Converted availability into Boolean values.
6. Converted GBP prices into INR using a fixed assumed exchange rate.
7. Stored the processed records in SQLite using related `books` and `categories` tables.
8. Performed SQL queries and compared SQL JOIN results with Pandas merge results.

## Data Cleaning and Quality Decisions

- Removed unwanted characters such as `Â` and `£` before converting prices to numeric values.
- Used `errors='coerce'` to convert invalid numeric prices into missing values for validation.
- Checked missing values and duplicate records before database insertion.
- Found five books with the source category label `Add a comment`. Replaced this invalid label with `Unknown` while preserving all five books.
- No invalid numeric prices or missing values were found in the collected 100 records.

## Currency Conversion

Used a fixed assumed conversion rate:

`1 GBP = ₹105.50`

This is a project assumption, not a live exchange rate. INR values were rounded to two decimal places.

## Database Design

The SQLite database contains two tables:

- `categories`: Stores unique category names.
- `books`: Stores book details and references categories through `category_id`.

A foreign key maintains the relationship between the two tables.

## SQL Analysis

The project includes queries for:

- Filtering books by price and rating.
- Sorting books by price.
- Finding distinct ratings.
- Filtering books within a price range.
- Joining books with categories.
- Counting books by category.
- Calculating average, minimum, and maximum prices.
- Checking database relationships.

The SQL JOIN output was compared with an equivalent Pandas merge, and both results matched.

## Validation Results

| Check | Result |
|---|---:|
| Books collected | 100 |
| Unique categories | 29 |
| Duplicate records | 0 |
| Missing values after cleaning | 0 |
| Books with corrected category | 5 |
| SQL JOIN and Pandas merge | Match |
| Foreign key errors | 0 |

## How to Run

Install the required libraries:

```bash
pip install requests pandas beautifulsoup4
