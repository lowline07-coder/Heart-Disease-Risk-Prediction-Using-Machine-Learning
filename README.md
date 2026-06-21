# Heart-Disease-Risk-Prediction-Using-Machine-Learning
Heart Disease Prediction using Python, Scikit-Learn, XGBoost, Data Analysis, Feature Engineering, and Classification Algorithms.
# ❤️ Heart Disease Prediction Using Machine Learning

## 📌 Project Overview

Heart Disease is one of the leading causes of death worldwide. Early prediction can assist healthcare professionals in identifying high-risk patients and taking preventive measures.

This project develops a Machine Learning Classification System that predicts whether a patient is likely to have heart disease based on various medical attributes such as age, blood pressure, cholesterol levels, heart rate, chest pain type, and ECG results.

The project follows a complete Machine Learning workflow including data cleaning, exploratory data analysis, feature engineering, model training, hyperparameter tuning, evaluation, and best model selection.

---

## 🎯 Project Objective

The primary objective of this project is to:

- Analyze patient health data.
- Identify important factors contributing to heart disease.
- Build multiple machine learning models.
- Compare model performance.
- Select the best-performing model for prediction.

---

## 📂 Dataset Information

Dataset: Heart Failure Prediction Dataset

Features include:

- Age
- Sex
- ChestPainType
- RestingBP
- Cholesterol
- FastingBS
- RestingECG
- MaxHR
- ExerciseAngina
- Oldpeak
- ST_Slope

Target Variable:

- HeartDisease
    - 0 = No Heart Disease
    - 1 = Heart Disease

---

# ⚙️ Project Workflow

## 1. Data Loading

- Imported dataset using Pandas.
- Examined structure and dimensions.

### Operations Performed

- head()
- shape
- info()
- describe()

---

## 2. Data Cleaning

Data quality issues were identified and corrected.

### Operations Performed

- Missing Value Detection
- Duplicate Record Detection
- Duplicate Removal
- Invalid Value Treatment

### Corrections Applied

- Cholesterol values equal to 0 replaced with median value.
- RestingBP values equal to 0 replaced with median value.

---

## 3. Exploratory Data Analysis (EDA)

EDA was conducted to understand distributions, trends, and relationships.

### Visualizations

- Target Variable Distribution
- Age Distribution
- Cholesterol Distribution
- Boxplots
- Correlation Heatmap

### Key Goals

- Identify patterns
- Detect outliers
- Understand feature relationships

---

## 4. Feature Engineering

Data transformation steps were performed before model training.

### Operations

#### Encoding

Categorical variables converted into numerical format using:

- One Hot Encoding

#### Scaling

Numerical features standardized using:

- StandardScaler

---

## 5. Train-Test Split

Dataset divided into:

- Training Data: 80%
- Testing Data: 20%

Purpose:

- Train model on unseen data.
- Evaluate generalization performance.

---

# 🤖 Machine Learning Models

## Logistic Regression

Used as a baseline classification model.

### Advantages

- Fast
- Interpretable
- Good baseline performance

---

## Decision Tree

Tree-based classification model capable of learning nonlinear patterns.

### Advantages

- Easy to understand
- Handles nonlinear relationships

---

## K-Nearest Neighbors (KNN)

Instance-based learning algorithm.

### Advantages

- Simple implementation
- Effective for local patterns

---

## Random Forest

Ensemble learning technique based on multiple decision trees.

### Advantages

- High accuracy
- Reduces overfitting
- Robust performance

---

## XGBoost

Gradient boosting algorithm widely used in machine learning competitions.

### Advantages

- High predictive power
- Efficient learning
- Excellent performance on structured data

---

# 🔧 Hyperparameter Tuning

GridSearchCV was used to optimize model parameters.

### Tuned Parameters

Random Forest:

- n_estimators
- max_depth

XGBoost:

- n_estimators
- max_depth

---

# 📊 Model Evaluation

Models were evaluated using:

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score
- Confusion Matrix

---

# 🏆 Best Model Selection

All models were compared based on their performance metrics.

Comparison Table Generated:

| Model | Accuracy |
|---------|---------|
| Logistic Regression | Evaluated |
| Decision Tree | Evaluated |
| KNN | Evaluated |
| Random Forest | Evaluated |
| XGBoost | Evaluated |

The model with the highest predictive performance was selected as the final model.

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost

## Development Environment

- Jupyter Notebook
- VS Code

---

# 📁 Project Structure

Heart-Disease-Prediction-ML-Classification-Project/

│

├── heart.csv

├── Heart_Disease_Final_Portfolio.ipynb

├── app.py

├── requirements.txt

├── README.md

│

├── images/

│ ├── countplot.png

│ ├── age_distribution.png

│ ├── heatmap.png

│

└── outputs/

├── model_comparison.png

└── confusion_matrix.png

---



# 📈 Results

The project successfully demonstrates the complete machine learning lifecycle from raw data preprocessing to model evaluation and selection.

Key achievements include:

- Comprehensive Data Cleaning
- Detailed Exploratory Data Analysis
- Feature Engineering Pipeline
- Multiple Classification Models
- Hyperparameter Optimization
- Comparative Performance Evaluation
- Best Model Selection

---

# 📚 Learning Outcomes

Through this project the following concepts were applied:

- Data Cleaning
- Data Visualization
- Feature Engineering
- Machine Learning Classification
- Hyperparameter Tuning
- Model Evaluation
- Performance Comparison
- End-to-End ML Workflow

---

# 👨‍💻 Author

Anuj Rasaily
