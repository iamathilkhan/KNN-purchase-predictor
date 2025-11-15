from flask import Flask, render_template, request
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load and train the model
df = pd.read_csv('Social_Network_Ads.csv')
x = df.drop('Purchased', axis=1)
y = df['Purchased']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = int(request.form['age'])
        salary = float(request.form['salary'])
        value = pd.DataFrame([{'Age': age, 'EstimatedSalary': salary}])
        prediction = model.predict(value)[0]
        result = 'Purchased' if prediction == 1 else 'Not Purchased'
        return render_template('result.html', result=result, age=age, salary=salary)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
