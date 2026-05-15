# 📈 Stock Price Predictor App

A machine learning-powered web application that predicts stock prices based on historical market data. 
The project explores time series forecasting techniques and presents predictions through an interactive interface.

## 🔍 Project Overview

This project uses machine learning techniques to analyze historical stock data and forecast future prices. 
It is designed to demonstrate how data science can be applied in financial markets to support decision-making.
The app allows users to input a stock symbol and visualize predicted trends compared to actual historical performance.

## ⚙️ Features

- 📊 Historical stock data visualization  
- 🤖 Machine learning-based price prediction  
- 📉 Trend forecasting over time  
- 🖥️ Interactive user interface (Streamlit / web app)  
- 🔄 Real-time prediction pipeline

## 🧠 Tech Stack

- Python   
- Pandas & NumPy  
- Scikit-learn
- TensorFlow
- Keras
- Matplotlib  
- Streamlit (for UI)
- Flask

## Table of Contents
- [Setup](#setup)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)

## Setup
Before you begin, ensure you have met the following requirements:

- Python 3.7 or later
- pip (Python package manager)

Clone the repository:
```bash
git clone https://github.com/kerubobosire254/Stock-Price-Prediction-API.git
cd Stock-Price-Prediction-API
```

## Installation
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

## API Documentation
### Base URL
For local development, the base URL is:
```
http://localhost:5000
```

### Endpoints
#### 1. Get Price Prediction
- **URL**: `/predict`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
      "stock_symbol": "AAPL",
      "date": "2026-04-22"
    }
    ```
- **Response**:
    ```json
    {
      "predicted_price": 150.25
    }
    ```

#### 2. Get Historical Data
- **URL**: `/historical`
- **Method**: `GET`
- **Query Parameters**:
    - stock_symbol: Symbol of the stock (e.g., AAPL)
    - start_date: Start date for historical data (YYYY-MM-DD)
    - end_date: End date for historical data (YYYY-MM-DD)
- **Response**:
    ```json
    {
      "data": [
        {
          "date": "2026-04-01",
          "closing_price": 145.30
        },
        ...
      ]
    }
    ```

## Deployment
1. **Run the Application**
    Start the API server by running:
    ```bash
    python app.py
    ```
    The API will be available at http://localhost:5000.

2. **Production Deployment**  
In production, run the application using Gunicorn:
gunicorn app:app

### Common Issues
- Model loading errors may occur if TensorFlow versions differ between training and deployment environments.
- Ensure compatibility between `.h5` model files and TensorFlow versions.
  
## Contributing
If you would like to contribute to the project, please make a pull request. Ensure that your code adheres to the project’s standards and has been adequately tested.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.  

## Contact
For any queries, please contact the project maintainer at kerubobosire254@example.com.
