import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/creditcard.csv")

print("=" * 60)
print("FINANCIAL FRAUD DETECTION PROJECT")
print("=" * 60)

print("\nDataset Shape:", df.shape)

print("\nFraud Distribution:")
print(df["Class"].value_counts())

# Plot Class Distribution
plt.figure(figsize=(6,4))
df["Class"].value_counts().plot(kind="bar")

plt.title("Fraud vs Normal Transactions")
plt.xlabel("Class")
plt.ylabel("Count")

plt.xticks([0,1], ["Normal", "Fraud"])

plt.tight_layout()

plt.show()