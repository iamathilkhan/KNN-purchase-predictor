# 🛒 KNN Purchase Predictor

<p align="center">
  <strong>An intelligent machine learning application that predicts customer purchase behavior using the K-Nearest Neighbors algorithm</strong>
  <br><br>
  <a href="#features">Features</a> •
  <a href="#technology-stack">Technology</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#project-structure">Structure</a>
</p>

---

## 📋 Overview

**KNN Purchase Predictor** is a machine learning classification application that leverages the **K-Nearest Neighbors (KNN)** algorithm to predict whether a customer will purchase an advertised product based on demographic features (age and estimated salary). This project demonstrates practical implementation of supervised learning for real-world customer behavior prediction.

### Use Cases
- 🎯 **Targeted Marketing** - Identify high-probability purchase customers
- 📊 **Customer Segmentation** - Classify customers into purchase likelihood groups
- 💼 **Business Intelligence** - Data-driven decision making for ad campaigns
- 🔍 **Behavioral Analysis** - Understand customer purchasing patterns

---

## ✨ Key Features

- 🤖 **K-Nearest Neighbors Classification** - Proven algorithm for customer prediction
- 🌐 **Web-Based Interface** - User-friendly Flask application for real-time predictions
- 📊 **Real-Time Analysis** - Instant prediction results with confidence metrics
- 🎯 **Social Network Dataset** - Trained on proven advertisement response data
- 📈 **Scalable Architecture** - Easy to integrate with larger datasets
- 💾 **Model Persistence** - Pre-trained model ready for inference
- 🔧 **Easy Setup** - Simple installation and deployment

---

## 📊 Dataset Information

| Aspect | Details |
|--------|---------|
| **Source** | Social Network Advertisements Dataset |
| **Samples** | 400 records |
| **Features** | 2 (Age, Estimated Salary) |
| **Target Variable** | Purchase Decision (Binary: Yes/No) |
| **Feature Range** | Age: 18-88 years, Salary: $15K-$150K |

---

## 🛠️ Technology Stack

![Python](https://img.shields.io/badge/-Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/-Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/iamathilkhan/KNN-purchase-predictor.git
cd KNN-purchase-predictor
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pandas scikit-learn flask numpy
```

---

## 📖 Usage

### Running the Application

1. **Start the Flask Server:**
   ```bash
   python app.py
   ```

2. **Open Web Browser:**
   - Navigate to: `http://127.0.0.1:5000/`

3. **Make Predictions:**
   - Enter your **Age** (18-88 years)
   - Enter your **Estimated Salary** ($15K-$150K)
   - Click **"Predict"** to get instant results

### Example Predictions

| Age | Salary | Prediction |
|-----|--------|------------|
| 25 | $30,000 | ❌ Not Likely |
| 45 | $120,000 | ✅ Likely |
| 35 | $50,000 | ❓ Uncertain |

---

## 📁 Project Structure

```
KNN-purchase-predictor/
├── app.py                    # Flask application
├── train_model.py            # Model training script
├── requirements.txt          # Python dependencies
├── data/
│   └── Social_Network_Ads.csv
├── models/
│   └── knn_model.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## 🔄 Algorithm Overview

**K-Nearest Neighbors (KNN) Process:**

```
Input: Age & Salary
  ↓
Feature Scaling (Normalization)
  ↓
Find K=5 Nearest Neighbors
  ↓
Analyze Neighbor Decisions
  ↓
Majority Vote Decision
  ↓
Output: Purchase Prediction
```

---

## 📊 Model Configuration

| Parameter | Value |
|-----------|-------|
| **Algorithm** | K-Nearest Neighbors |
| **K Value** | 5 |
| **Distance Metric** | Euclidean |
| **Expected Accuracy** | 85-92% |

---

## 🔧 Customization

### Adjust K Value
```python
# In app.py or train_model.py
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=7)  # Change K value
```

### Add More Features
- Location-based data
- Social network connections
- Purchase history
- Time of day factors

---

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 5000 already in use | `python app.py --port 8000` |
| ModuleNotFoundError | `pip install -r requirements.txt` |
| Poor accuracy | Adjust K value or add features |

---

## 📚 Resources

- [Scikit-learn KNN Documentation](https://scikit-learn.org/stable/modules/neighbors.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [K-Nearest Neighbors Algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)

---

## 📝 License

This project is open source and available under the **MIT License**.

---

## 📬 Support

- **Email:** athilkhan2005@gmail.com
- **LinkedIn:** [Connect here](https://linkedin.com/in/ahamed-athil-khan)
- **GitHub Issues:** [Report issues](https://github.com/iamathilkhan/KNN-purchase-predictor/issues)

---

<p align="center">
  <b>⭐ If you found this useful, please give it a star! ⭐</b>
  <br>
  <sub>Made with ❤️ by Ahamed Athil Khan</sub>
</p>
