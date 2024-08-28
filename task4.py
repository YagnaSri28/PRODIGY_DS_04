import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
training_data = pd.read_csv('/content/twitter_training.csv')
validation_data = pd.read_csv('/content/twitter_validation.csv')

# Rename the columns for better understanding
training_data.columns = ['ID', 'Brand', 'Sentiment', 'Tweet']
validation_data.columns = ['ID', 'Brand', 'Sentiment', 'Tweet']

# Plot sentiment distribution for training data
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.countplot(data=training_data, x='Sentiment', palette='viridis')
plt.title('Sentiment Distribution in Training Data')
plt.xlabel('Sentiment')
plt.ylabel('Count')

# Plot sentiment distribution for validation data
plt.subplot(1, 2, 2)
sns.countplot(data=validation_data, x='Sentiment', palette='viridis')
plt.title('Sentiment Distribution in Validation Data')
plt.xlabel('Sentiment')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

# Plot sentiment distribution for each brand in training data
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
sns.countplot(data=training_data, x='Brand', hue='Sentiment', palette='viridis')
plt.title('Sentiment Distribution by Brand in Training Data')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.xticks(rotation=90)

# Plot sentiment distribution for each brand in validation data
plt.subplot(1, 2, 2)
sns.countplot(data=validation_data, x='Brand', hue='Sentiment', palette='viridis')
plt.title('Sentiment Distribution by Brand in Validation Data')
plt.xlabel('Brand')
plt.ylabel('Count')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()
