from flask import Flask, request, render_template
import joblib
import numpy as np
import os
import json
import plotly
import plotly.graph_objects as go

app = Flask(__name__)

# Load the trained model (expects 3 features: test preparation, reading score, writing score)
model_path = 'webapp/student_performance_model.pkl'
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input values from the form (3 features expected)
        study_prep = int(request.form['study_prep'])      # Expected as 0 (None) or 1 (Completed)
        reading_score = float(request.form['reading_score'])
        writing_score = float(request.form['writing_score'])
    except ValueError:
        return render_template('result.html', prediction_text="Invalid input. Please enter valid numbers.")

    # Prepare input for prediction
    input_features = np.array([[study_prep, reading_score, writing_score]])
    prediction = model.predict(input_features)[0]
    prediction_value = round(prediction, 2)

    # ---------- Interactive Visualization with Plotly ----------
    # Create an interactive bar chart comparing Reading Score, Writing Score, and Predicted Math Score
    fig = go.Figure(data=[go.Bar(x=['Reading Score', 'Writing Score', 'Predicted Math Score'],
                                 y=[reading_score, writing_score, prediction_value],
                                 marker_color=['#4CAF50', '#2196F3', '#FF9800'])])
    fig.update_layout(title='Input Scores vs. Predicted Math Score',
                      xaxis_title='Feature',
                      yaxis_title='Score')
    # Convert the Plotly figure to JSON so it can be rendered in the template
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('result.html',
                           prediction_text=f"Predicted Math Score: {prediction_value}",
                           graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)
