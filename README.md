# Walmart-Sales
Walmart Weekly Sales Forecasting
This project provides a robust, end-to-end workflow for forecasting Walmart’s weekly sales using advanced machine learning models: Random Forest, XGBoost, and LightGBM. The workflow includes data cleaning, feature engineering, model training, evaluation, and business insights, with a focus on reproducibility and clarity.

Project Structure
Features
Data Cleaning & EDA: Handles missing values, outliers, and explores key trends.
Feature Engineering: Time-based, lag, rolling, interaction, and categorical features.
Model Training: Modular functions for Random Forest, XGBoost, and LightGBM.
Evaluation: RMSE, MAE, and R² metrics for fair comparison.
Visualization: Actual vs. predicted plots, feature importance, and error analysis.
Reproducibility: All code and requirements are documented for easy reuse.
How to Use
Install dependencies:

Run the notebooks in order:

data_cleaning.ipynb → Random_Forest.ipynb / XGBOOST.ipynb / LightGBM.ipynb → Comparision.ipynb
Use the models.py functions for modular model training and evaluation in your own scripts or notebooks.

Requirements
All dependencies are listed in requirements.txt and documented in Requirements.ipynb.

Results
LightGBM achieved the best performance (lowest RMSE and MAE, highest R²).
All models provide strong predictive accuracy, but LightGBM is recommended for deployment.
License
This project is for educational and demonstration purposes.

Feel free to copy, modify, and expand this README for your GitHub repository!
