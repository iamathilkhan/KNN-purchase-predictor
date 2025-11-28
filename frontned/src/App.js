import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [age, setAge] = useState('');
  const [salary, setSalary] = useState('');
  const [prediction, setPrediction] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const response = await axios.post('http://localhost:5000/api/predict', {
        age: parseInt(age),
        salary: parseFloat(salary)
      });
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Error making prediction:', error);
      setError('Unable to make prediction. Please check your input and try again.');
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>KNN Purchase Predictor</h1>
        <p>Enter your details to predict if you'll make a purchase</p>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="age">Age:</label>
            <input
              type="number"
              id="age"
              value={age}
              onChange={(e) => setAge(e.target.value)}
              placeholder="Enter your age"
              required
              min="18"
              max="100"
            />
          </div>
          <div className="form-group">
            <label htmlFor="salary">Estimated Salary ($):</label>
            <input
              type="number"
              id="salary"
              value={salary}
              onChange={(e) => setSalary(e.target.value)}
              placeholder="Enter your estimated salary"
              required
              min="0"
              step="1000"
            />
          </div>
          <button type="submit" disabled={loading}>
            {loading ? 'Predicting...' : 'Predict Purchase'}
          </button>
        </form>
        {prediction && (
          <div className="prediction-result">
            <p>Prediction: <strong>{prediction}</strong></p>
          </div>
        )}
        {error && (
          <div className="prediction-result">
            <p className="error-message">{error}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
