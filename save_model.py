import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
 
np.random.seed(42)
num_samples = 200

data = {
    'N': np.random.randint(10, 140, num_samples),
    'P': np.random.randint(10, 100, num_samples),
    'K': np.random.randint(10, 200, num_samples),
    'temperature': np.random.uniform(15, 40, num_samples),
    'humidity': np.random.uniform(30, 100, num_samples),
    'ph': np.random.uniform(4.5, 8.5, num_samples),
    'rainfall': np.random.uniform(50, 300, num_samples)
}

df = pd.DataFrame(data)

crops = ['rice', 'maize', 'chilli', 'cotton', 'coffee']
df['crop'] = np.random.choice(crops, num_samples)

X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['crop']

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("SUCCESS: Your model.pkl file has been generated and saved!")
