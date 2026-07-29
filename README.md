# Final Project: Vehicle Safety Recall Analysis (2014–2024)

### Isabella Castle

### Fall 2025

## About

This project explores whether domestic car manufacturers (Ford, Chevrolet, Chrysler) are more or less recall-prone than international manufacturers (Toyota, Honda, Hyundai) between the years 2014 and 2024. It: 

- Uses U.S. vehicle safety recall patterns using data from the National Highway Traffic Safety Administration (NHTSA) API.
- Acquires said recall data.
- Cleans and organizes it into a sql database containing two tables.
- Analyzes recall trends.

## How To Use

1) Install Python dependencies (requests, pandas, sqlite3, matplotlib, plotnine)
2) Run scripts/acquire_data.py to download raw data from the API (already completed — raw data stored in data/raw/)
3) Open Analysis.ipynb and run all cells

## Final Findings

This project found that from 2014–2024, domestic manufacturers consistently had significantly more safety recalls than international manufacturers, peaking at over 200 recalls per year. International brands remained much lower and more stable.
(See “Final Analysis & Conclusion”  in "Analysis.ipynb" for more details)
