Rossmann Pharmaceuticals Sales Forecasting
Project Overview
The Rossmann Pharmaceuticals Sales Forecasting project aims to predict store sales using historical sales data, promotional information, and store-specific features. Accurate sales forecasting is crucial for optimizing inventory management, improving customer satisfaction, and making informed business decisions.

Table of Contents
Technologies Used
Installation
Usage
Data Description
Modeling Approach
Results
Contributing
License
Technologies Used
Python
Pandas
NumPy
Scikit-Learn
XGBoost
Matplotlib
Seaborn
Jupyter Notebook
Installation
To set up the project environment, follow these steps:
Clone the Repository:


git clone https://github.com/eliasgirmah/week_four.git
cd week_four
Create a Virtual Environment:


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Required Packages:


pip install -r requirements.txt
Usage
Data Preparation:
Ensure that the dataset is in the correct format and placed in the data/ directory.

Run the Jupyter Notebook:

bash

jupyter notebook sales_forecasting.ipynb
View Results:
Follow the notebook cells to view data processing, EDA (Exploratory Data Analysis), and model evaluation results.

Data Description
The dataset includes the following columns:

Store: Unique store identifier.
Sales: Daily sales (target variable).
Customers: Number of customers that visited the store.
Promo: Indicates whether a promotion was running that day.
StateHoliday: Indicates if the day is a state holiday.
SchoolHoliday: Indicates if the day is a school holiday.
Date: The date of the recorded data.
CompetitionOpenSinceYear: Year when a competing store opened.
CompetitionOpenSinceMonth: Month when a competing store opened.
Promo2SinceYear: Year when Promo2 started.
Promo2SinceWeek: Week when Promo2 started.
Modeling Approach
The modeling process consists of the following steps:

Data Cleaning:

Handle missing values.
Convert date columns to datetime format for easier processing.
Feature Engineering:

Create new features such as WeekOfYear, CompetitionOpenNumMonths, and Promo2NumWeeks to capture temporal and promotional effects.
Train-Test Split:

Split the data into training (80%) and testing (20%) sets to validate model performance.
Model Selection:

Evaluate various models such as Linear Regression, Random Forest, and XGBoost, as well as Deep Learning techniques to predict sales accurately.
Model Evaluation:

Use performance metrics such as:
RMSE (Root Mean Squared Error)
MAE (Mean Absolute Error)
R² score (Coefficient of Determination)