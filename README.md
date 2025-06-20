# 🛒 BigMart Sales Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![Machine Learning](https://img.shields.io/badge/ML-Regression-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Project Overview

This project predicts sales for BigMart outlets using machine learning regression algorithms. The application features an interactive web interface built with Streamlit, allowing users to input various parameters and get real-time sales predictions.

## 🎯 Business Problem

BigMart is one of the largest retail chains with outlets across different cities. The company wants to predict sales for each product in different outlets to optimize inventory management and improve business decision-making.

## 🔍 Key Features

- **Interactive Web Application**: User-friendly Streamlit interface
- **Real-time Predictions**: Instant sales forecasting based on input parameters
- **Multiple Input Factors**: Considers item characteristics, outlet demographics, and historical data
- **Professional UI**: Clean design with visual elements and formatted output
- **Model Deployment**: Serialized ML model for efficient predictions

## 📊 Dataset Features

The model considers the following input parameters:

| Feature | Description | Type |
|---------|-------------|------|
| Item_Fat_Content | Fat content of the item (Low Fat/Regular) | Categorical |
| Item_Type | Category of the item | Categorical |
| Item_Weight | Weight of the item | Numerical |
| Item_Visibility | Visibility percentage of item in store | Numerical |
| Item_MRP | Maximum Retail Price of item | Numerical |
| Outlet_Identifier | Unique identifier for outlet | Categorical |
| Outlet_Size | Size of the outlet (Small/Medium/High) | Categorical |
| Outlet_Location_Type | Type of location (Tier 1/2/3) | Categorical |
| Outlet_Type | Type of outlet (Supermarket Type1/2/3) | Categorical |
| Outlet_Establishment_Year | Year outlet was established | Numerical |

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework
- **Scikit-learn**: Machine learning library
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Pickle**: Model serialization
- **PIL (Pillow)**: Image processing

## 📁 Project Structure

```
BigMart-Sales-Prediction/
│
├── Frontend/
│   ├── Bigmart_Sales_Prediction.py    # Main Streamlit application
│   └── bank.png                       # UI image asset
│
├── Model/
│   └── ML_Model_Bigmart_Sales.pkl     # Trained ML model
│
├── Data/                              # Dataset directory
│   ├── train.csv                      # Training data
│   └── test.csv                       # Test data
│
├── Notebooks/                         # Jupyter notebooks
│   ├── Data_Analysis.ipynb            # Exploratory data analysis
│   └── Model_Training.ipynb           # Model development
│
├── requirements.txt                   # Dependencies
├── README.md                          # Project documentation
└── LICENSE                           # License file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/Lkanth05/Big-Mart-Sales-Prediction.git
cd Big-Mart-Sales-Prediction
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
# Navigate to Frontend directory
cd Frontend

# Run Streamlit application
streamlit run Bigmart_Sales_Prediction.py
```

The application will open in your default web browser at `http://localhost:8501`

## 🎮 How to Use

1. **Launch the Application**: Run the Streamlit app using the commands above
2. **Input Parameters**: Fill in the required fields:
   - Select item fat content (Low Fat/Regular)
   - Choose item type from dropdown
   - Select outlet characteristics
   - Enter numerical values for weight, visibility, MRP, and establishment year
3. **Get Prediction**: Click the "Submit" button to get sales prediction
4. **View Results**: The predicted sales amount will be displayed in Indian Rupees

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | [Add your algorithm name] |
| Training Accuracy | [Add your accuracy] |
| R² Score | [Add R² score] |
| RMSE | [Add RMSE value] |
| MAE | [Add MAE value] |

*Note: Add your actual model performance metrics here*

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)

### Prediction Results
![Prediction Results](screenshots/prediction_results.png)

*Note: Add actual screenshots of your application*

## 🔧 Model Details

### Data Preprocessing
- Handled missing values using appropriate imputation techniques
- Encoded categorical variables using label encoding
- Feature scaling applied where necessary
- Outlier detection and treatment

### Model Training
- Split data into training and testing sets (80:20 ratio)
- Applied cross-validation for model evaluation
- Hyperparameter tuning using grid search
- Model serialization using Pickle

### Feature Engineering
- Created derived features from existing variables
- Handled categorical variables with proper encoding
- Feature selection based on importance scores

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Future Enhancements

- [ ] Add more advanced ML algorithms (Random Forest, XGBoost)
- [ ] Implement feature importance visualization
- [ ] Add model comparison dashboard
- [ ] Include confidence intervals for predictions
- [ ] Deploy on cloud platforms (Heroku, AWS)
- [ ] Add data validation and error handling
- [ ] Implement A/B testing framework

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Lkanth05**
- GitHub: [@Lkanth05](https://github.com/Lkanth05)
- LinkedIn: [Add your LinkedIn profile]

## 🙏 Acknowledgments

- BigMart for providing the dataset
- Streamlit team for the amazing framework
- Open source community for the tools and libraries

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub or contact me directly.

---

⭐ **Star this repository if you found it helpful!** ⭐
