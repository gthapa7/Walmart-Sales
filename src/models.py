"""
Model training functions for Walmart Weekly Sales Forecasting.
Includes Random Forest, XGBoost, and LightGBM regressors.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from xgboost import XGBRegressor
import lightgbm as lgb


def train_random_forest(X_train, y_train, params=None):
    """Train a Random Forest Regressor."""
    if params is None:
        params = {'n_estimators': 100, 'max_depth': 10, 'random_state': 42, 'n_jobs': -1}
    model = RandomForestRegressor(**params)
    model.fit(X_train, y_train)
    return model


def train_xgboost(X_train, y_train, params=None):
    """Train an XGBoost Regressor."""
    if params is None:
        params = {'objective': 'reg:squarederror', 'random_state': 42}
    model = XGBRegressor(**params)
    model.fit(X_train, y_train)
    return model


def train_lightgbm(X_train, y_train, params=None):
    """Train a LightGBM Regressor."""
    if params is None:
        params = {
            'objective': 'regression',
            'metric': 'rmse',
            'num_leaves': 31,
            'learning_rate': 0.05,
            'n_estimators': 100,
            'feature_fraction': 0.8,
            'verbose': -1
        }
    model = lgb.LGBMRegressor(**params)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """Return RMSE, MAE, and R2 for a fitted model."""
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return {'RMSE': rmse, 'MAE': mae, 'R2': r2}
