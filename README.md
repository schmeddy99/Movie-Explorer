# 🎬 Movie Explorer

A fun and educational command-line tool for searching, analyzing, and discovering movies using a real-world dataset.
Built with **Python** and **SQLite**, this project demonstrates practical use of SQL queries, data normalization, CLI design, and export features.

---

## 🧱 Project Layout

```bash
movie_project/
│
├── main.py                # Main entry point (runs everything)
├── schema.py              # All CREATE TABLE statements
├── import_data.py         # Code to import & clean CSV data
├── queries/               # All SQL logic
│   ├── queries.py         # Core search and analytics queries
│   └── fun_queries.py     # Fun/random discovery queries
├── utils.py               # Helpers for I/O, data cleaning, exports
├── menus.py               # CLI menu handlers
├── data/
│   └── movie_metadata.csv # CSV dataset
└── movie.db               # SQLite database file (auto-generated)
```

---

## 📊 Dataset

- **Source**: [IMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset)
- **File**: `data/movie_metadata.csv`

---

## 🌟 Features

### ⌕ Search

- Search movies by:
  - Title
  - Director
  - Genre
  - Year
  - IMDb Rating Threshold

### 📊 Insights

- Top-rated movies
- Average IMDb score by genre
- Movie count per decade
- Most frequent director
- Average gross by country

### 🌈 Discovery

- Random movie picker
- Random movie by genre or decade
- Longest movie title
- Most common word in genres
- Total word count in titles

### 🔍 Export

- Export results to **JSON** or **HTML** files

---

## 🚀 How to Run

1. Clone this repo:

```bash
git clone https://github.com/yourusername/movie-explorer.git
cd movie-explorer
```

2. Make sure Python is installed
3. Run the app:

```bash
python main.py
```

---

## 📅 Example

```
Choose an option:
1. Search
2. Insights
3. Discovery
4. Exit
Command: 1

Enter a movie title to search: inception

🔍 Matching Titles:
Inception | 2010
```

---

## 🌐 Live Demo

[Run on Replit](https://replit.com/join/okgxnoiwra-ahmedaosman00)

---

## 📝 .gitignore

```
__pycache__/
*.pyc
movie.db
*.json
*.html
```

---

## 📚 Educational Value

- SQL: Joins, aggregates, filtering, normalization
- Python: Functions, modules, CLI design, file I/O
- Clean project architecture with separation of concerns

---

## 🙏 Acknowledgements

Special thanks to [Yueming](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset?resource=download) for publishing the IMDb 5000 Movie Dataset.

---
