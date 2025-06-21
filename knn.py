import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,accuracy_score

df = pd.read_csv('C:/Users/athin/OneDrive/Desktop/AI projects/Social_Network_Ads.csv')

x = df.drop('Purchased', axis=1) 
y = df['Purchased']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

value = pd.DataFrame([{
    'Age': int(input('Enter Age: ')),
    'EstimatedSalary': float(input('Enter Estimated Salary: ')),
}])

predicted_purchase = model.predict(value)
print(f"Predicted Purchase: {'Purchased' if predicted_purchase[0] == 1 else 'Not Purchased'}")