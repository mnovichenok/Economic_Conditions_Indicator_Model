# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from scipy.stats import chi2_contingency, boxcox
from imblearn.over_sampling import SMOTE  # Import SMOTE

# %%
data1 = pd.read_csv("./data/index_economic_activity.csv")
data2 = pd.read_csv("./data/CPI_percent_change.csv")
data3 = pd.read_csv("./data/CLI.csv")
data3.head()

# %%
# % Change In CLI
data3['% Change CLI'] = data3['CLI'].pct_change() * 100
data3['% Change CLI'] = data3['% Change CLI'].fillna(0)
data3 = data3.rename(columns={'Month3': 'Month'})

# %%
#DATA CLEANING
# create copy of the dataset
df = pd.concat([data1, data2, data3], axis=1)
df = df.rename(columns={'All Items': '% Change CPI'})
df['% Change CPI'] = df['% Change CPI'].str.rstrip('%').astype(float)
df = df.loc[:,~df.columns.duplicated()].copy() #drop extra 'Month' columns
df.drop(df.tail(3).index, inplace=True) #drop three last rows where CLI data is missing

# %%
### 'Expansion':0; 'Slowdown':1; 'Recession':2; 'Recovery':3;

def categorize_CLI_change(row):
    cli = row['CLI']
    cli_change = row['% Change CLI']
    
    if cli_change>=0 and cli>=100:
        return 0
    elif cli_change<0 and cli>=100:
        return 1
    elif cli_change<0 and cli<100:
        return 2
    elif cli_change>=0 and cli<100:
        return 3

df['Regime'] = df.apply(categorize_CLI_change, axis=1)
df.head()

# %%
#DATA PREPROCESSING
#variable X equal to the numerical features and a variable y equal to the "RiskLevel" column.
X = df.drop('Regime', axis=1).values
y = df['Regime'].values

y = y.astype(int)

#split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101, stratify=y)

#feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

X_train = X_train_resampled
y_train = y_train_resampled



