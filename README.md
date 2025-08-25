# Walmart-Sales
Walmart Weekly Sales Forecasting

This project provides a robust, end-to-end workflow for forecasting Walmart’s weekly sales using advanced machine learning models: Random Forest, XGBoost, and LightGBM.

The workflow covers data cleaning, feature engineering, model training, evaluation, and business insights with a strong focus on reproducibility and clarity.

📂 Project Structure

Data Cleaning & EDA

Handles missing values and outliers

Explores key sales trends

Feature Engineering

Time-based features (Year, Month, Week, etc.)

Lag & rolling statistics

Interaction & categorical features

Model Training

Modular functions for Random Forest, XGBoost, and LightGBM

Evaluation

Metrics: RMSE, MAE, R²

Fair model comparison

Visualization

Actual vs. predicted plots

Feature importance

Error analysis

Reproducibility

All code and requirements are documented for easy reuse

⚙️ How to Use
1. Install dependencies
pip install -r requirements.txt

2. Run the notebooks in order

data_cleaning.ipynb

Random_Forest.ipynb / XGBOOST.ipynb / LightGBM.ipynb

Comparision.ipynb

3. Use modular functions

The models.py script contains reusable functions for training and evaluating models in your own notebooks or scripts.

📦 Requirements

All dependencies are listed in requirements.txt

Detailed explanation in Requirements.ipynb

📊 Results

LightGBM achieved the best performance:

Lowest RMSE & MAE

Highest R²

All models provide strong predictive accuracy, but LightGBM is recommended for deployment.

📜 License

This project is for educational and demonstration purposes.
Feel free to copy, modify, and expand this repository.
