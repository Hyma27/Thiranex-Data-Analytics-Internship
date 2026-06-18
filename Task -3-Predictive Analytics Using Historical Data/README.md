# 🌊 Water Demand Prediction 

## 📌 Project Overview

The Water Demand Prediction System is a Predictive Analytics project that forecasts water consumption trends using historical water usage data. The project applies data preprocessing, exploratory data analysis (EDA), machine learning models, and visualization techniques to understand factors affecting water demand and predict future consumption.

---

## 🎯 Objectives

- Analyze historical water consumption data.
- Clean and preprocess the dataset.
- Perform Exploratory Data Analysis (EDA).
- Build predictive models using machine learning.
- Compare model performance using evaluation metrics.
- Identify important factors influencing water consumption.

---

## 📊 Dataset Information

The dataset contains 500 records with the following features:

- Country
- Year
- Total Water Consumption (Billion Cubic Meters)
- Per Capita Water Use (Liters per Day)
- Agricultural Water Use (%)
- Industrial Water Use (%)
- Household Water Use (%)
- Rainfall Impact (Annual Precipitation in mm)
- Groundwater Depletion Rate (%)
- Water Scarcity Level

### Target Variable

**Total Water Consumption (Billion Cubic Meters)**

---

## 🔧 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle

---

## 📈 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Dataset Overview
- Missing Value Analysis
- Duplicate Record Analysis
- Correlation Heatmap
- Water Consumption Trend Analysis
- Feature Importance Analysis

---

## 🤖 Machine Learning Models

### 1. Linear Regression

Used as the baseline predictive model.

### 2. Random Forest Regressor

Used for ensemble-based prediction and feature importance analysis.

### 3. Gradient Boosting Regressor

Used to compare performance with other regression models.

---

## 📊 Model Performance

| Model             | MAE   | RMSE   | R² Score |
| ----------------- | ----- | ------ | --------- |
| Linear Regression | 75.46 | 97.83  | -0.002    |
| Random Forest     | 77.52 | 101.77 | -0.084    |
| Gradient Boosting | 80.69 | 106.89 | -0.196    |

### Best Model

**Linear Regression**

---

## 📌 Key Findings

- Household Water Use (%) was the most important feature.
- Groundwater Depletion Rate (%) strongly influenced water consumption.
- Industrial and Agricultural Water Use contributed significantly.
- Water Scarcity Level had minimal impact on prediction performance.
- Weak correlations among features resulted in limited predictive accuracy.

---

## 📁 Project Structure

```text
Water_Demand_Prediction/
│
| └── cleaned_global_water_consumption.csv
│
├── water_demand_prediction.ipynb
│
├── linear_regression_model.pkl
│
├── README.md
│
└── requirements.txt
```

---

## 💾 Model Saving

The final Linear Regression model was saved using Pickle:

```python
import pickle

with open("linear_regression_model.pkl", "wb") as file:
    pickle.dump(model, file)
```

---

## 🚀 Future Enhancements

- Use larger real-world datasets.
- Apply advanced models such as XGBoost and LSTM.
- Develop a Streamlit dashboard for interactive forecasting.
- Integrate real-time weather and environmental data.

---

## 🎓 Learning Outcomes

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Regression Modeling
- Model Evaluation
- Predictive Analytics
- Data Visualization

---

## 📜 Conclusion

This project successfully demonstrated the complete Predictive Analytics workflow using historical water consumption data. Multiple machine learning models were trained and evaluated to forecast water demand trends. Although prediction accuracy was limited due to weak relationships among features, the project provided valuable insights into water consumption patterns and factors affecting demand.
