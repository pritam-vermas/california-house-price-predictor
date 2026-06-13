# 🌸 Iris Flower Classification

### 🚀 Live Demo

**Try the Project Here:**
https://huggingface.co/spaces/pritamvermas/iris-flower-classification

---

## 📌 Project Overview

This project is a Machine Learning-based Flower Classification System that predicts the species of an Iris flower using its physical measurements.

The model classifies flowers into one of the following three species:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

The application is built using **Python**, **Scikit-Learn**, and **Gradio**, and is deployed on **Hugging Face Spaces**.

---

## 🎯 Objective

The objective of this project is to:

* Perform Exploratory Data Analysis (EDA) on the Iris dataset.
* Visualize relationships between different flower features.
* Train Machine Learning models for classification.
* Compare model performance.
* Predict flower species based on user input.
* Deploy the trained model with an interactive web interface.

---

## 📊 Dataset Information

The project uses the famous Iris Dataset containing 150 flower samples.

### Features

| Feature      | Description          |
| ------------ | -------------------- |
| Sepal Length | Length of sepal (cm) |
| Sepal Width  | Width of sepal (cm)  |
| Petal Length | Length of petal (cm) |
| Petal Width  | Width of petal (cm)  |

### Target Variable

| Species         |
| --------------- |
| Iris-setosa     |
| Iris-versicolor |
| Iris-virginica  |

---

## 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

* Dataset shape analysis
* Missing value detection
* Statistical summary
* Class distribution analysis
* Pairplot visualization
* Correlation heatmap
* Scatter plots
* Feature relationship analysis

### Key Findings

* Iris-setosa is clearly separable from other species.
* Petal Length and Petal Width are the most important features.
* Petal Length and Petal Width show a very strong positive correlation.
* Versicolor and Virginica have slight overlap in some feature combinations.

---

## 🤖 Machine Learning Models Used

### 1. Logistic Regression

A linear classification algorithm used for multi-class classification.

### 2. Decision Tree Classifier

A tree-based algorithm that classifies samples using decision rules.

---

## 📈 Model Performance

| Model                    | Accuracy |
| ------------------------ | -------- |
| Logistic Regression      | 100%     |
| Decision Tree Classifier | 100%     |

Both models achieved perfect classification accuracy on the test dataset.

---

## 🔥 Confusion Matrix Analysis

The confusion matrix showed:

* Correct classification of all test samples.
* No misclassifications.
* Perfect prediction performance on the test dataset.

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Gradio
* Hugging Face Spaces

---

## 🚀 How to Run Locally

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/iris-flower-classification.git
cd iris-flower-classification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 🌐 Web Application Features

* Interactive user interface
* Real-time prediction
* Simple and beginner-friendly design
* Fast model inference
* Deployed on Hugging Face Spaces

---

## 📝 Example Prediction

### Input

```text
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2
```

### Output

```text
Iris-setosa
```

---

## 📂 Project Structure

```text
iris-flower-classification/
│
├── app.py
├── iris_model.pkl
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author

**Pritam Verma**

Machine Learning Intern

---

## ⭐ Conclusion

This project successfully demonstrates the complete Machine Learning workflow including data analysis, visualization, model training, evaluation, prediction, and deployment. The final application provides an easy-to-use interface for predicting Iris flower species based on flower measurements.
