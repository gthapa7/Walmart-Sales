# Walmart Weekly Sales Forecasting

This project provides a **robust, end-to-end workflow** for forecasting Walmart’s weekly sales using advanced machine learning models: **Random Forest, XGBoost, and LightGBM**.

The workflow covers **data cleaning, feature engineering, model training, evaluation, and business insights** with a strong focus on **reproducibility and clarity**.

---

## 🔄 Project Structure
```
.
├── Walmart.csv              # Raw data file
├── data_cleaning.ipynb      # Data cleaning and EDA notebook
├── Random_Forest.ipynb      # Random Forest modeling notebook
├── XGBOOST.ipynb            # XGBoost modeling notebook
├── LightGBM.ipynb           # LightGBM modeling notebook
├── Comparision.ipynb        # Model comparison and visualization
├── Requirements.ipynb       # Documentation of requirements and imports
├── requirements.txt         # All dependencies for easy setup
└── src/
    ├── __init__.py          # Initialization module
    └── models.py            # Model training and evaluation functions
```
---

## 🧹 Data Cleaning and Exploratory Data Analysis (EDA)

- Handles missing values and outliers
- Explores key sales trends

---

## ⚙️ Feature Engineering

- Creates time-based features (Year, Month, Week, etc.)
- Implements lag & rolling statistics
- Includes interaction & categorical features

---

## 🧠 Model Training

- Focuses on modular functions for Random Forest, XGBoost, and LightGBM

---

## 📊 Evaluation Metrics

- **Metrics used:** RMSE, MAE, R²
- Ensures fair model comparison

---

## 📈 Data Visualization

- Includes actual vs. predicted plots
- Highlights feature importance
- Performs error analysis

---

## 🔄 Reproducibility

- All code and dependencies are documented for easy reusability
---

## 📦 Requirements

- Install dependencies from `requirements.txt`
- Details are explained in `Requirements.ipynb`

---

## 🏆 Results Overview

- **Best performer:** LightGBM achieved the best performance with:
  - Lowest RMSE & MAE
  - Highest R²

---

## 📜 License

This project was created for **educational and demonstration purposes** only. Feel free to **fork, modify, and enhance**.

---

## ⚙️ How to Use

1. **Clone this repository**:
    ```bash
    git clone https://github.com/gthapa7/Walmart-Sales.git
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run notebooks in sequence**:
    - `data_cleaning.ipynb`
    - Choose one: `Random_Forest.ipynb` / `XGBOOST.ipynb` / `LightGBM.ipynb`
    - Finally: `Comparision.ipynb`

4. **Leverage modular functions from `models.py`**:
    - Simply import the utilities provided for custom implementations.

---