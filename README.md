# Olivetti Faces Classification MLOps Project

This project implements an end-to-end Machine Learning pipeline for classifying images from the Olivetti faces dataset. It features a Flask web application for inference, Docker containerization, Kubernetes deployment configurations, and a fully automated CI/CD pipeline using GitHub Actions.

## 📂 Code Overview

* **`train.py`**: Fetches the dataset, trains a `DecisionTreeClassifier`, and serializes the model and test data to `savedmodel.pth`.
* **`test.py`**: Loads the trained model from `savedmodel.pth` and evaluates its accuracy on the test set.
* **`app.py`**: A Flask web server that exposes a UI for image uploading and performs inference using the trained model.
* **`Dockerfile`**: Encapsulates the application environment (Python 3.10) and dependencies, configuring Gunicorn to serve the app.
* **`kubernetes/deployment.yaml`**: Defines the Kubernetes resources (Deployment and Service) to orchestrate the application.

---

## ⚙️ GitHub Actions Workflow (CI)

The project utilizes **GitHub Actions** for Continuous Integration, ensuring that code changes are automatically tested. The workflow configuration is located at `.github/workflows/ci.yml`.

**Trigger**:
* The pipeline runs automatically on every `push` event to any branch.

**Pipeline Steps**:
1.  **Environment Setup**: Provisions an Ubuntu runner and sets up Python 3.10.
2.  **Dependency Installation**: Upgrades `pip` and installs all libraries listed in `requirements.txt`.
3.  **Training Validation**: Executes `train.py` to verify that the model training pipeline completes successfully and generates the `savedmodel.pth` artifact.
4.  **Testing**: Executes `test.py` to perform inference on the test set and print accuracy metrics, ensuring the model functions correctly.

---

## 🚀 Usage Instructions

### 1. Local Setup
1.  **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Train the model**:
    ```bash
    python train.py
    ```
3.  **Run the web app**:
    ```bash
    python app.py
    ```

### 2. Docker Usage
1.  **Build the image**:
    ```bash
    docker build -t olivetti-face-app .
    ```
2.  **Run the container**:
    ```bash
    docker run -p 5000:5000 olivetti-face-app
    ```

### 3. Kubernetes Deployment
1.  **Apply manifests**:
    ```bash
    kubectl apply -f kubernetes/deployment.yaml
    ```
2.  **Access**:
    The service is exposed via a LoadBalancer on port 80 (mapping to container port 5000).
