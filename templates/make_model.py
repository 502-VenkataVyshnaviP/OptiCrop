import pickle
from sklearn.linear_model import LogisticRegression
import numpy as np

# Create a dummy model
model = LogisticRegression()
X = np.random.rand(10, 7)
y = ['rice', 'maize', 'chilli', 'cotton', 'coffee', 'rice', 'maize', 'chilli', 'cotton', 'coffee']
model.fit(X, y)

# Save it as model.pkl
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Success! Created model.pkl in your folder.")
