from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load and train the model
df = pd.read_csv('Social_Network_Ads.csv')
x = df.drop('Purchased', axis=1)
y = df['Purchased']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

@app.route('/api/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = app.make_default_options_response()
        return response
    try:
        data = request.get_json()
        age = int(data['age'])
        salary = float(data['salary'])
        value = pd.DataFrame([{'Age': age, 'EstimatedSalary': salary}])
        prediction = model.predict(value)[0]
        result = 'Purchased' if prediction == 1 else 'Not Purchased'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
