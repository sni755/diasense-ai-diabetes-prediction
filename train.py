import os
import json
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ==========================================
# 1. CREATE OUTPUT FOLDERS
# ==========================================

os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# ==========================================
# 2. LOAD DATASET
# ==========================================

DATA_PATH = "data/diabetes_binary_health_indicators_BRFSS2015.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset loaded successfully!")
print("Dataset shape:", df.shape)

# ==========================================
# 3. CLEAN DATA
# ==========================================

if "ID" in df.columns:
    df = df.drop(columns=["ID"])

TARGET = "Diabetes_binary"

if TARGET not in df.columns:
    raise ValueError(
        f"'{TARGET}' column was not found."
    )

X = df.drop(columns=[TARGET])
y = df[TARGET]

print("\nFeatures:", len(X.columns))
print("Target:", TARGET)

# ==========================================
# 4. TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# ==========================================
# 5. RANDOM FOREST PIPELINE
# ==========================================

model = Pipeline([
    (
        "imputer",
        SimpleImputer(strategy="median")
    ),

    (
        "scaler",
        StandardScaler()
    ),

    (
        "random_forest",
        RandomForestClassifier(
            n_estimators=250,
            max_depth=12,
            min_samples_split=4,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        )
    )
])

# ==========================================
# 6. TRAIN
# ==========================================

print("\nTraining Random Forest...")

model.fit(X_train, y_train)

print("Training complete!")

# ==========================================
# 7. PREDICTIONS
# ==========================================

y_pred = model.predict(X_test)

y_probability = model.predict_proba(X_test)[:, 1]

# ==========================================
# 8. EVALUATION
# ==========================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

roc_auc = roc_auc_score(
    y_test,
    y_probability
)

metrics = {
    "Accuracy": round(float(accuracy), 4),
    "Precision": round(float(precision), 4),
    "Recall": round(float(recall), 4),
    "F1-Score": round(float(f1), 4),
    "ROC-AUC": round(float(roc_auc), 4)
}

# ==========================================
# 9. PRINT RESULTS
# ==========================================

print("\n================================")
print("MODEL PERFORMANCE")
print("================================")

for name, value in metrics.items():
    print(f"{name}: {value}")

# ==========================================
# 10. SAVE METRICS
# ==========================================

with open(
    "outputs/metrics.json",
    "w"
) as file:

    json.dump(
        metrics,
        file,
        indent=4
    )

# ==========================================
# 11. ROC CURVE
# ==========================================

fpr, tpr, _ = roc_curve(
    y_test,
    y_probability
)

plt.figure(figsize=(8, 6))

plt.plot(
    fpr,
    tpr,
    label=f"Random Forest (AUC = {roc_auc:.3f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

plt.title("ROC-AUC Curve")

plt.legend()

plt.tight_layout()

plt.savefig(
    "outputs/roc_curve.png",
    dpi=300
)

plt.close()

# ==========================================
# 12. CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(
    y_test,
    y_pred
)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[
        "Non-Diabetic",
        "Diabetic"
    ]
)

fig, ax = plt.subplots(
    figsize=(7, 6)
)

display.plot(
    ax=ax,
    values_format="d"
)

plt.title("Confusion Matrix")

plt.tight_layout()

plt.savefig(
    "outputs/confusion_matrix.png",
    dpi=300
)

plt.close()

# ==========================================
# 13. SAVE FEATURE NAMES
# ==========================================

features = X.columns.tolist()

with open(
    "models/features.json",
    "w"
) as file:

    json.dump(
        features,
        file,
        indent=4
    )

# ==========================================
# 14. SAVE TRAINED MODEL
# ==========================================

joblib.dump(
    model,
    "models/diabetes_rf_pipeline.joblib"
)

print("\n================================")
print("PROJECT FILES CREATED")
print("================================")

print("✓ Model")
print("✓ Feature list")
print("✓ Metrics")
print("✓ ROC curve")
print("✓ Confusion matrix")

print("\nTraining finished successfully! 🎉")