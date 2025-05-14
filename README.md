# Economic Conditions Indicator Model
## A Multi-Class Logistic Regression Classifier in Python/NumPy

This project implements a multi-class logistic regression model from scratch using Python and NumPy to classify the macroeconomic regime of the U.S. economy. The model distinguishes between four economic states:

#### Expansion, Slowdown, Recession, and Recovery

The model achieves a 92% accuracy rate and uses key macroeconomic indicators including:

- OECD Composite Leading Indicator (CLI)
- Consumer Price Index (CPI) % Change
- Economic activity metrics (e.g., business applications, construction spending, durable goods orders, trade flows, retail and wholesale inventories)

## Regime Classification Criteria
Regimes are determined based on the OECD’s framework for interpreting CLI values:
- Expansion	CLI > 100 and rising;	Economy is growing above trend
- Slowdown	CLI > 100 and falling;	Growth is decelerating but remains above trend
- Recession	CLI < 100 and falling;	Economy is contracting below trend
- Recovery	CLI < 100 and rising;	Economy is improving but still below long-term trend

##### Sources:

Organisation for Economic Co-operation and Development (OECD). Interpreting OECD Composite Leading Indicators (CLIs). OECD, Oct. 2020, https://www.oecd.org/content/dam/oecd/en/data/methods/Interpreting_OECD_Composite_Leading_Indicators.pdf.

Organisation for Economic Co-operation and Development (OECD). OECD System of Composite Leading Indicators. OECD, Apr. 2012, https://www.oecd.org/content/dam/oecd/en/data/methods/OECD-System-of-Composite-Leading-Indicators.pdf.

## Model Details
Framework: One-vs-All Logistic Regression (Multi-Class)

Features Used:
- CLI level and CLI monthly change
- CPI percent change
- Business and trade activity indicators, Retail/wholesale inventories, Housing and construction statistics, etc.

Balancing: SMOTE (Synthetic Minority Oversampling Technique)

Optimization: Gradient Descent

Tuning: Parametric Grid Search for learning rate, regularization strength (epsilon), maximum iterations

## Results

<img width="442" alt="Screenshot 2025-05-14 at 12 05 10 PM" src="https://github.com/user-attachments/assets/f1dcc379-6249-43f7-9e14-a5172750b1a5" />
<img width="650" alt="Screenshot 2025-05-14 at 12 07 35 PM" src="https://github.com/user-attachments/assets/e13ab386-7b0d-4efd-9ece-1f738b325ffc" />
<img width="523" alt="Screenshot 2025-05-14 at 12 07 52 PM" src="https://github.com/user-attachments/assets/6783c124-5ba2-4817-8fcb-821df3ae9427" />


### -Maya Novichenok
