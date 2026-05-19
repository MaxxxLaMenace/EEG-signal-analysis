import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# =========================
# 1. Charger le dataset
# =========================
df = pd.read_csv("data/dataset.csv")

# =========================
# 2. Séparer features / target
# =========================
# Remplace "target" par le nom de ta colonne à prédire
X = df.drop(columns=["target"])
y = df["target"]

# =========================
# 3. Split train / test
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# 4. Créer le modèle
# =========================
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

# =========================
# 5. Entraîner
# =========================
model.fit(X_train, y_train)

# =========================
# 6. Prédictions
# =========================
y_pred = model.predict(X_test)

# =========================
# 7. Évaluation
# =========================
print("Accuracy :", accuracy_score(y_test, y_pred))

print("\nClassification report :")
print(classification_report(y_test, y_pred))

# =========================
# 8. Importance des features
# =========================
print("\nImportance des features :")

for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature}: {importance:.4f}")