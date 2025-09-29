#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv("azureml://subscriptions/<sub-id>/resourcegroups/<customer>-workshop/workspaces/amlhuduaworkshop/datastores/experimentation/paths/output-folder/ml-experimentation/*")
df


# In[4]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb


# In[5]:


# Encode the target variable
label_encoder = LabelEncoder()
df['approved'] = label_encoder.fit_transform(df['approved'])  # Yes=1, No=0

# Define features and target
X = df[['AGE', 'avgcost']]
y = df['approved']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=42)

# Train XGBoost model
model = xgb.XGBClassifier()
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")


# In[ ]:




