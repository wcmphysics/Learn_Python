import numpy as np
import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression

# --- 1. Setup: Create and save a dummy model for demonstration ---
# We train on a DataFrame so the model captures feature names
X_train = pd.DataFrame(np.random.rand(10, 3), columns=['temp', 'humidity', 'wind_speed'])
y_train = np.random.rand(10)

model = LinearRegression()
model.fit(X_train, y_train)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# --- 2. Loading the model ---
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# --- 3. Verification Logic ---
def verify_features(model, df):
    """
    Verifies that the DataFrame contains the correct features.
    Returns a DataFrame with columns reordered to match the model's training order.
    """
    if not hasattr(model, 'feature_names_in_'):
        print("Warning: Model does not have 'feature_names_in_'. Skipping verification.")
        return df

    expected_features = list(model.feature_names_in_)
    current_features = list(df.columns)

    # Check for missing features
    missing = set(expected_features) - set(current_features)
    if missing:
        raise ValueError(f"Missing features in input data: {missing}")

    # Check for extra features (optional warning)
    extra = set(current_features) - set(expected_features)
    if extra:
        print(f"Note: Input data contains extra features that will be ignored: {extra}")

    # Reorder columns to match the model's training order
    return df[expected_features]

# --- 4. Execution ---
# New data with shuffled column order
df_new = pd.DataFrame([[0.5, 0.2, 0.8]], columns=['humidity', 'wind_speed', 'temp'])

# Step A: Verification
df_verified = verify_features(loaded_model, df_new)
print("Verification successful. Features reordered.")

# Step B: Prediction
predictions = loaded_model.predict(df_verified)
print(f"Predictions: {predictions}")
