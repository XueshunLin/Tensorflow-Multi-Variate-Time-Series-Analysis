# Time Series Anomaly Detection and Forecasting
<a target="_blank" href="https://colab.research.google.com/github/Yagami11111/Tensorflow-Muti-Variate-Time-Series-Analysis/blob/main/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Project Overview

This project depict a sub anomaly detection system of a Smart Hybrid Quantum Task Scheduler, appear in the right half image of the system structure below    
![image-structure](https://github.com/Yagami11111/Tensorflow-Muti-Variate-Time-Series-Analysis/blob/main/pictures/structure.png)    

The system focused on time series anomaly detection and forecasting to enhance the availability of quantum computers. It includes phases such as data loading, preprocessing, anomaly detection, and forecasting using various models. The goal is to create accurate models for detecting anomalies in IoT sensor data and forecasting future values, ultimately developing a forecasting-boosted anomaly detection system.       

Training and deploying process described in the graphs below.  
![image-structure](https://github.com/Yagami11111/Tensorflow-Muti-Variate-Time-Series-Analysis/blob/main/pictures/training.png)
![image-structure](https://github.com/Yagami11111/Tensorflow-Muti-Variate-Time-Series-Analysis/blob/main/pictures/deploying.jpg)    

**Technologies:** Python, Pandas, NumPy, Seaborn, Matplotlib, Scipy, Scikit-learn, PyOD, TensorFlow, Keras, Keras Tuner

## Directory Structure

- `data_loading.py`: Script for loading data.
- `data_preprocessing.py`: Script for preprocessing the data.
- `databases/`: Directory containing database files.
  - `cd230831.db`: Data start from 08/31/2023
  - `cd230926.db`: Data start from 09/26/2023
  - `cd240111.db`: Data start from 01/11/2024
- `db_definition.py`: Script defining database schema.
- `hypermodels/`: Directory for hyperparameter tuning models, containing hyperparameters and weights.
  - `lstm_ad/`
  - `lstm_forecast/`
  - `nbeats_forecast/`
- `main.ipynb`: Jupyter notebook for the main analysis.
- `naive_anomaly_detection.py`: Script for naive anomaly detection.
- `pictures/`: Directory for pics of the project structure.
- `processed_datasets/`: Directory for generated datasets during processing.
- `README.md`: This README file.
- `saved_models/`: Directory for saved models.
  - `AD_model/` Trained LSTM Auto-Encoder model
    - `xgb_model.pkl`Trained XGB model
- `Technical Report.pdf`: Detailed technical report of the project.
- `visualization.py`: Script for data visualization.

## Data Description

The dataset for this project was collected from IoT sensors affixed on Quantum computers in the laboratory. Data was aggregated in real-time in an time-series database

## Anomaly Detection

### Models and Methods

- **Naive Anomaly Detection Method:** A simple method using gradients and moving averages to detect anomalies.
- **Classification Model with Manual Labels:** A random forest model trained on manually labeled data.
- **Isolation Forest:** An unsupervised machine learning model for anomaly detection.
- **Local Outlier Factor (LOF):** A density-based anomaly detection model.
- **LSTM Auto-Encoder:** A deep learning model for detecting anomalies based on reconstruction loss.

### Benchmarks and Metrics

The performance of anomaly detection models was evaluated using Excess-Mass (EM) and Mass-Volume (MV) metrics, introduced by Nicolas(2016).

## Time Series Forecasting

### Models and Methods

- **LSTM Forecasting Model:** A model using LSTM layers to forecast future values.
- **N-BEATS:** A non-recurrent neural network architecture for time-series forecasting.
- **XGBoost:** A gradient boosting model adapted for time series forecasting.
- **ARIMA:** A classical statistical model for time series forecasting.

### Benchmarks and Metrics

The forecasting models were evaluated on unseen test data using metrics such as MAE, MSE, RMSE, and MAPE.

## Technical report
For details of the design, please check the technical report.
