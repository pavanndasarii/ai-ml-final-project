# Titanic Survival Analysis and Machine Learning

## Objective

Analyze the Titanic passenger dataset and develop machine learning classification models to predict passenger survival.

## Project Workflow

- Exploratory Data Analysis (EDA)
- Data cleaning and missing value handling
- Analysis of passenger survival patterns
- Feature selection and preprocessing
- Categorical feature encoding and numerical feature scaling
- Model training and evaluation
- Hyperparameter tuning using GridSearchCV
- Feature importance analysis

## Machine Learning Models

Three classification models were developed:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

## Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

### Model Results

| Model | Accuracy | F1-score | ROC-AUC |
|---|---:|---:|---:|
| Logistic Regression | 0.8045 | 0.7244 | 0.8437 |
| Decision Tree | 0.8156 | 0.7556 | 0.7967 |
| Random Forest | 0.8156 | 0.7442 | 0.8271 |

The original Decision Tree achieved the highest F1-score among the three original models.

## Hyperparameter Optimization

GridSearchCV with 5-fold cross-validation was used to test 45 Decision Tree hyperparameter combinations.

The tuned model was compared with the original Decision Tree. The original model was retained because it achieved a higher test F1-score.

## Feature Importance

Feature importance analysis identified sex, age, fare, and passenger class as influential features in the Decision Tree model.

## Project Files

- `01_eda.ipynb` – Exploratory Data Analysis
- `02_modeling.ipynb` – Data preprocessing, model training, evaluation, hyperparameter tuning, and feature importance
- `titanic.csv` – Dataset used for modeling

## Libraries and Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab
- Git and GitHub

## Conclusion

This project demonstrates an end-to-end machine learning workflow, including exploratory data analysis, data preprocessing, classification, model evaluation, hyperparameter optimization, and model interpretation.
