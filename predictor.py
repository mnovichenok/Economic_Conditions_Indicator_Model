from logistic_regression import logisticRegression  
from data import df, scaler, X_train, X_test, y_train, y_test  
import numpy as np
from datetime import datetime
from itertools import product
from sklearn.metrics import accuracy_score


# %%
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from typing import Optional

# %%
#grid search
learning_rates = [0.5, 0.1, 0.05, 0.01, 0.001]
max_iters_list = [200, 250, 500, 700, 1000]
epsilons = [1e-2, 1e-4, 1e-6]

best_params = None
best_score = 0

for lr, max_iter, eps in product(learning_rates, max_iters_list, epsilons):
    model = logisticRegression(learning_rate=lr, max_iters=max_iter, epsilon=eps)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    if acc > best_score:
        best_score = acc
        best_params = (lr, max_iter, eps)


# %%
now = datetime.now()
current_year = now.year
current_month = now.month

mean = df.mean()
feature_defaults = {
    "Year": current_year,
    "Month": current_month,
    "BusinessApplications": mean['BusinessApplications'],
    "ConstructionSpending":  mean['ConstructionSpending'],
    "DurableGoodsNewOrders":  mean['DurableGoodsNewOrders'],
    "InternationalTrade_Exports":  mean['InternationalTrade_Exports'],
    "InternationalTrade_Imports":  mean['InternationalTrade_Imports'],
    "ManuInventories":  mean['ManuInventories'],
    "ManuNewOrders":  mean['ManuNewOrders'],
    "NewHomesForSale":  mean['NewHomesForSale'],
    "NewHomesSold":  mean['NewHomesSold'],
    "ResConstPermits":  mean['ResConstPermits'],
    "ResConstUnitsCompleted":  mean['ResConstUnitsCompleted'],
    "ResConstUnitsStarted":  mean['ResConstUnitsStarted'],
    "RetailInventories":  mean['RetailInventories'],
    "SalesForRetailAndFood":  mean['SalesForRetailAndFood'],
    "WholesaleInventories":  mean['WholesaleInventories'],
    "PercentChangeCPI":  mean['% Change CPI'],
    "CLI": mean['CLI'],
    "PercentChangeCLI":  mean['% Change CLI']
}

# %%
ordered_keys = [
    "Year", "Month", "BusinessApplications", "ConstructionSpending",
    "DurableGoodsNewOrders", "InternationalTrade_Exports", "InternationalTrade_Imports",
    "ManuInventories", "ManuNewOrders", "NewHomesForSale", "NewHomesSold",
    "ResConstPermits", "ResConstUnitsCompleted", "ResConstUnitsStarted",
    "RetailInventories", "SalesForRetailAndFood", "WholesaleInventories",
    "PercentChangeCPI", "CLI", "PercentChangeCLI"
]

# %%
app = FastAPI()

class Economic_Data(BaseModel) :
    Year: Optional[int]
    Month: Optional[int]
    BusinessApplications: Optional[float]
    ConstructionSpending: Optional[float]
    DurableGoodsNewOrders: Optional[float]
    InternationalTrade_Exports: Optional[float]
    InternationalTrade_Imports: Optional[float]
    ManuInventories: Optional[float]
    ManuNewOrders: Optional[float]
    NewHomesForSale: Optional[float]
    NewHomesSold: Optional[float]
    ResConstPermits: Optional[float]
    ResConstUnitsCompleted: Optional[float]
    ResConstUnitsStarted: Optional[float]
    RetailInventories: Optional[float]
    SalesForRetailAndFood: Optional[float]
    WholesaleInventories: Optional[float]
    PercentChangeCPI: Optional[float]
    CLI: Optional[float]
    PercentChangeCLI: Optional[float]

# %%
@app.post("/data/")
def get_econ_data(data : Economic_Data):
    model = logisticRegression(learning_rate=best_params[0], max_iters=best_params[1], epsilon=best_params[2])
    model.fit(X_train, y_train)

    user_input = data.dict()
    all_features = {}
    for key in feature_defaults:
        if user_input.get(key) == None:
            all_features[key] = feature_defaults[key]
        else:
            all_features[key] = user_input.get(key)

    input_array = np.array([all_features[key] for key in ordered_keys]).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    pred = model.predict(input_scaled)[0]
    regimes = ["Expansion", "Slowdown", "Recession", "Recovery"]
    return {"regime": regimes[pred]}
