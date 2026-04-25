# 🔥 Algerian Forest Fires Prediction Model

A machine learning application that predicts forest fire probability in Algeria using Ridge Regression. This project includes a web interface built with Flask for easy predictions.

## 📋 Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Technologies](#technologies)
- [Contributing](#contributing)

---

## ✨ Features

- **Machine Learning Model**: Ridge Regression for accurate fire probability prediction
- **Web Interface**: User-friendly Flask web application with HTML forms
- **Data Preprocessing**: StandardScaler for feature normalization
- **Model Serialization**: Pre-trained models saved as pickle files for quick deployment
- **RESTful API**: POST endpoint for predictions
- **Responsive UI**: HTML templates for intuitive user interaction

---

## 📁 Project Structure

```
s-by-s-ml-project/
├── application.py                          # Main Flask application
├── model_training.ipynb                    # Model training notebook
├── EDA_FE.ipynb                            # Exploratory Data Analysis & Feature Engineering
├── Algerian_forest_fires_cleaned_dataset.csv
├── Algerian_forest_fires_dataset_UPDATE.csv
├── ridge.pkl                               # Trained Ridge Regression model
├── scaler.pkl                              # StandardScaler for feature normalization
├── templates/
│   ├── index.html                          # Home page
│   └── home.html                           # Prediction form & results page
└── README.md
```

---

## 📊 Dataset

The project uses the Algerian Forest Fires dataset containing:
- **Features**: Temperature, Relative Humidity (RH), Wind Speed (Ws), Rainfall, FFMC, DMC, ISI, Classes, Region
- **Target**: Forest fire probability/severity
- **Preprocessing**: Data cleaning, feature scaling, and outlier handling
- **Files**: 
  - `Algerian_forest_fires_cleaned_dataset.csv` - Cleaned version
  - `Algerian_forest_fires_dataset_UPDATE.csv` - Updated raw data

---

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/shreyas927/s-by-s-ml-project.git
cd s-by-s-ml-project
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install flask numpy pandas scikit-learn
```

---

## 💻 Usage

### Run the Flask Application

```bash
python application.py
```

The application will start at `http://localhost:5000/`

### Making Predictions

1. Open the web browser and navigate to `http://localhost:5000/`
2. Fill in the forest fire parameters:
   - Temperature
   - Relative Humidity (RH)
   - Wind Speed (Ws)
   - Rainfall
   - FFMC Index
   - DMC Index
   - ISI Index
   - Classes
   - Region

3. Click **Predict** to get the fire probability

### API Endpoint

**POST** `/predict`

```bash
curl -X POST http://localhost:5000/predict \
  -d "Temperature=25&RH=50&Ws=10&Rain=0&FFMC=85&DMC=100&ISI=5&Classes=1&Region=1"
```

---

## 🤖 Model Details

- **Algorithm**: Ridge Regression
- **Features**: 9 input features (temperature, humidity, wind speed, rainfall, fire indices)
- **Preprocessing**: StandardScaler normalization
- **Model File**: `ridge.pkl`
- **Scaler File**: `scaler.pkl`

### Training Process

Refer to `model_training.ipynb` for:
- Data loading and exploration
- Feature engineering
- Model training and evaluation
- Hyperparameter tuning

### Exploratory Data Analysis

Refer to `EDA_FE.ipynb` for:
- Dataset statistics
- Correlation analysis
- Data visualization
- Feature importance

---

## 🛠️ Technologies

| Technology | Purpose |
|-----------|---------|
| **Flask** | Web framework |
| **Scikit-learn** | Machine Learning |
| **Pandas** | Data manipulation |
| **NumPy** | Numerical computations |
| **HTML** | Frontend UI |
| **Pickle** | Model serialization |

---

## 📈 Model Performance

The Ridge Regression model provides:
- Fast inference times
- Regularization to prevent overfitting
- Reliable fire probability predictions
- Scalable for production deployment

---

## 🔄 Workflow

1. **Data Collection** → Load datasets
2. **EDA & Feature Engineering** → Analyze and prepare features
3. **Model Training** → Train Ridge Regression model
4. **Model Evaluation** → Validate performance
5. **Deployment** → Serve predictions via Flask API
6. **User Interface** → Interact with model predictions

---

## 📝 Files Description

| File | Description |
|------|-------------|
| `application.py` | Main Flask app with routing and prediction logic |
| `ridge.pkl` | Trained Ridge Regression model |
| `scaler.pkl` | Feature normalization scaler |
| `model_training.ipynb` | Complete model training pipeline |
| `EDA_FE.ipynb` | Data exploration and feature analysis |
| `templates/index.html` | Homepage |
| `templates/home.html` | Prediction interface |

---

## 💡 Future Improvements

- [ ] Deploy to cloud (AWS)

**Created by**: Shreyas