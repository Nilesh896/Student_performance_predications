# Student Performance Prediction

## 📌 Project Overview
This project is a **machine learning web application** that predicts students' math scores based on their study preparation, reading, and writing scores. The model uses **Linear Regression** and provides an interactive web interface using **Flask**.

## ✨ Features
- Predicts math scores based on **reading and writing scores** + **test preparation status**.
- Interactive **Plotly visualizations** comparing actual input vs. predicted scores.
- **User-friendly UI** with input forms and graphical outputs.
- Model trained using **Linear Regression** with optimized parameters.
- Deployed on **Render** for free public access.

## 📁 Project Structure
```
student-performance-ml/
├── data/                  # Dataset (CSV files)
├── model/                 # Trained ML model (Pickle file)
├── notebooks/             # Jupyter Notebooks for EDA & model training
├── webapp/                # Flask Web Application
│   ├── app.py             # Main Flask backend
│   ├── templates/         # HTML templates
│   │   ├── index.html     # Home Page
│   │   ├── result.html    # Prediction result page
│   ├── static/            # CSS, JS, and images
├── requirements.txt       # Required Python libraries
├── Procfile               # Deployment process file
├── README.md              # Project documentation (this file)
```

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/student-performance-ml.git
cd student-performance-ml
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run Flask Application
```sh
cd webapp
python app.py
```
The app should be running on **http://127.0.0.1:5000/**.

## 🚀 Deployment on Render
### 1️⃣ Push Your Code to GitHub
Make sure your project is **pushed to a GitHub repository**.

### 2️⃣ Set Up Render Web Service
- Go to [Render](https://render.com/) and create a **new web service**.
- Connect your **GitHub repository**.
- Set **Build Command:**
  ```sh
  pip install -r requirements.txt
  ```
- Set **Start Command:**
  ```sh
  gunicorn webapp.app:app
  ```
- Click **Deploy** and wait for the build to complete!

### 3️⃣ Access Your App
Once deployed, Render will provide a **public URL** (e.g., `https://your-app.onrender.com`).

## 📊 Model & Performance
- **Algorithm Used:** Linear Regression
- **Evaluation Metrics:**
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - R² Score
- **Feature Importance:** Reading & Writing scores have the highest correlation with math scores.


## 🤝 Contributing
Feel free to **fork** this repository and submit **pull requests** with improvements or additional features!

## 📄 License
This project is licensed under the MIT License.

---
📌 **Author:** Nilesh Yadav
📌 **GitHub:** [Your GitHub Profile](https://github.com/Nilesh896)
