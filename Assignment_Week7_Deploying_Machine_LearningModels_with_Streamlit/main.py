import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

# Ensure folder exists
os.makedirs(".", exist_ok=True)

# Load dataset
df = pd.read_csv("iris.csv")

# Encode species if needed
if df['species'].dtype == 'object':
    df['species'] = df['species'].astype('category').cat.codes

# Features and target
X = df.drop('species', axis=1)
y = df['species']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Accuracy
accuracy = accuracy_score(y_test, model.predict(X_test)) * 100
print(f"Model trained with accuracy: {accuracy:.2f}%")

# Save model
with open("classifier.pkl", "wb") as f:
    pickle.dump(model, f)

print(" Model saved as classifier.pkl")
