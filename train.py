# train.py
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib


def load_data(test_size=0.3, random_state=42):
    """Load Olivetti faces dataset and split into train/test."""
    data = fetch_olivetti_faces()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test


def main():
    X_train, X_test, y_train, y_test = load_data()

    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Save both model and test set so test.py can reuse them
    joblib.dump(
        {"model": clf, "X_test": X_test, "y_test": y_test},
        "savedmodel.pth"
    )

    # Optional quick check
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"[train.py] Quick test accuracy: {acc:.4f}")


if __name__ == "__main__":
    main()