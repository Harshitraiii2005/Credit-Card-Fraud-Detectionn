# 💳 Credit Card Fraud Detection  

🚀 **AI-powered fraud detection system** using **Machine Learning** to identify fraudulent credit card transactions.  
Built with **Streamlit** for an interactive UI and **Random Forest Model** for real-time fraud detection.

---

## 📂 Project Structure  

📦 Credit-Card-Fraud-Detection
┣ 📂 models/ # Trained ML model
┣ 📂 dataset/ # Dataset used for training
┣ 📂 images/ # GIFs and UI assets
┣ 📜 app.py # Main Streamlit app
┣ 📜 requirements.txt # Dependencies
┣ 📜 README.md # Documentation
┗ 📜 best_model_rf.pkl # Trained Random Forest model


---

## 📊 Dataset Information  

We use the **Credit Card Fraud Detection Dataset** from Kaggle:  
🔗 [Download Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)  

- **Transactions:** 284,807  
- **Fraudulent Cases:** 492 (~0.172%)  
- **Features:** 30 (Time, Amount, and 28 PCA-transformed variables)  
- **Imbalanced Data:** Requires special handling (SMOTE, anomaly detection, etc.)  

---

## ⚡ Features  

✅ **Fraud Detection** - Predict if a transaction is fraud or legitimate  
✅ **Risk Analysis** - Shows probability of fraud for better decision-making  
✅ **Interactive UI** - Built with **Streamlit** and **3D GIFs** for a modern feel  
✅ **Explainability Dashboard** - See why a transaction is flagged as fraud  
✅ **Real-time Prediction** - Enter transaction details and get instant results  

---

## 🛠️ Installation & Setup  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Harshitraiii2005/Credit-Card-Fraud-Detectionn.git
cd Credit-Card-Fraud-Detection


2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Application
bash
Copy
Edit
streamlit run app.py
🖥️ Tech Stack
Machine Learning Model: Random Forest
Frontend: Streamlit
Backend: Python
Libraries: NumPy, Pandas, Scikit-learn, Joblib, Matplotlib
🎨 UI Preview


🚀 Future Enhancements
🔹 Deploy API for fraud detection
🔹 Add advanced fraud explainability (SHAP values, LIME)
🔹 Use Deep Learning (LSTM/Autoencoders) for better fraud detection

👨‍💻 Developed by Harshit Rai
⭐ Star the repo if you like it! ⭐
📩 Feel free to contribute or suggest improvements!



