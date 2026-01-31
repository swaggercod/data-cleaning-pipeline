# E-Commerce Data Cleaning Pipeline

A comprehensive Python-based data cleaning pipeline for e-commerce datasets, implementing industry-standard data quality practices.

## 📋 Project Overview

This project demonstrates end-to-end data cleaning techniques using **Pandas** and **NumPy**. It processes raw e-commerce data with common real-world quality issues and produces a clean, analysis-ready dataset.

## 🎯 Features

- **Column Standardization**: Normalize column names (lowercase, underscore-separated)
- **Missing Value Handling**: Intelligent strategies for null values based on data type
- **Text Normalization**: Standardize text formatting (case, whitespace)
- **Data Validation**: Remove invalid records (negative prices, invalid ratings, etc.)
- **Duplicate Removal**: Identify and remove duplicate rows

## 🗂️ Project Structure

```
data-cleaning-pipeline/
├── data/
│   ├── raw/                  # Raw, uncleaned data
│   │   └── ecommerce_raw_data.csv
│   └── cleaned/              # Cleaned, processed data
│       └── ecommerce_cleaned_data.csv
├── src/
│   ├── generate_sample_data.py    # Generate sample dataset
│   ├── explore_data.py            # Data exploration script
│   └── data_cleaner.py            # Main cleaning pipeline
├── notebooks/                # Jupyter notebooks (optional)
├── tests/                    # Unit tests (future)
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical operations

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/data-cleaning-pipeline.git
cd data-cleaning-pipeline
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Generate sample data** (optional)
```bash
python src/generate_sample_data.py
```

## 🚀 Usage

### Run the complete pipeline:

```bash
python src/data_cleaner.py
```

### Or use individual functions:

```python
from src.data_cleaner import clean_data_pipeline

# Clean your data
df_cleaned = clean_data_pipeline(
    input_path='data/raw/your_data.csv',
    output_path='data/cleaned/your_data_cleaned.csv'
)
```

## 📊 Data Cleaning Steps

### 1. **Clean Column Names**
- Convert to lowercase
- Replace spaces with underscores
- Example: `Customer Name` → `customer_name`

### 2. **Handle Missing Values**
| Column Type | Strategy | Reason |
|------------|----------|--------|
| Numerical (price, quantity) | Fill with **median** | Not affected by outliers |
| Categorical (category) | Fill with **mode** | Most frequent value |
| Critical (email, date) | **Drop rows** | Essential fields |
| Customer name | Fill with 'Unknown' | Preserve records |

### 3. **Normalize Text**
- Strip leading/trailing whitespace
- Standardize case (Title case for names, lowercase for categories)
- Example: `"ELECTRONICS"` → `"electronics"`

### 4. **Remove Invalid Data**
- **Price**: Remove if ≤ 0
- **Quantity**: Remove if ≤ 0
- **Rating**: Keep only 1-5 range
- **Email**: Remove if missing '@' symbol

### 5. **Remove Duplicates**
- Identify duplicate rows
- Keep first occurrence
- Remove subsequent duplicates

## 📈 Results

**Before Cleaning:**
- 1,050 rows
- 662 missing values
- 45+ duplicate rows
- Invalid data (negative prices, invalid ratings)
- Inconsistent text formatting

**After Cleaning:**
- ~628 clean rows
- 0 missing values ✅
- 0 duplicates ✅
- 0 invalid records ✅
- Standardized formatting ✅

## 📝 Example

```python
import pandas as pd
from src.data_cleaner import (
    clean_column_names,
    handle_missing_values,
    normalize_text_columns,
    remove_invalid_data,
    remove_duplicates
)

# Load data
df = pd.read_csv('data/raw/ecommerce_raw_data.csv')

# Apply cleaning steps
df = clean_column_names(df)
df = handle_missing_values(df)
df = normalize_text_columns(df)
df = remove_invalid_data(df)
df = remove_duplicates(df)

# Save cleaned data
df.to_csv('data/cleaned/output.csv', index=False)
```

## 🧪 Testing

Run the test suite:

```bash
python src/data_cleaner.py
```

This will execute all cleaning functions and display detailed logs.

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Pandas data manipulation techniques
- ✅ Handling missing data strategies
- ✅ Data validation and quality checks
- ✅ Text processing and normalization
- ✅ Duplicate detection and removal
- ✅ Writing clean, documented Python code
- ✅ Project structure best practices

## 🔮 Future Enhancements

- [ ] Add unit tests with pytest
- [ ] Implement data profiling reports
- [ ] Add date parsing and validation
- [ ] Create interactive dashboard with Streamlit
- [ ] Add logging functionality
- [ ] Support for multiple file formats (Excel, JSON)
- [ ] Automated data quality scoring

## 👤 Author

**Your Name**
- GitHub: [@swaggercod](https://github.com/swaggercod)
- LinkedIn: [yusuf-ozturk](https://www.linkedin.com/in/yusuf-ozturk-561880367/)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Sample data generation inspired by real-world e-commerce datasets
- Built as a learning project for data engineering fundamentals

---

⭐ **If you find this project helpful, please give it a star!** ⭐
