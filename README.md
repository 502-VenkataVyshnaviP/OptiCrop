# OptiCrop: Smart Agricultural Production Optimization Engine

OptiCrop is an end-to-end data-driven production engine designed to advance precision agriculture and eliminate guesswork in farming. By integrating tabular soil metrics and macro climatic variables, the platform leverages state-of-the-art predictive machine learning models to provide intelligent crop recommendations, helping farmers optimize resource efficiency and maximize harvest yields.

---

## 👥 Core Project Team
* **Venkata Vyshnavi Pachipala** — *Team Lead*
* **Divya Teja Pattem** — *team member*
* **Shilpa Reddy** — *team member*
* **Tejaswini Sudha** — *team member*

---

## 📖 Project Overview & Mission
The main goal of **OptiCrop** is to revolutionize traditional agricultural practices by providing an advanced software suite that models complex crop-environment interactions. By interpreting a specific multi-variable matrix—including Nitrogen (N), Phosphorous (P), Potassium (K) levels, soil temperature, humidity, pH, and rainfall—the application provides automated, evidence-based recommendations. The insights generated assist farmers, agricultural researchers, policymakers, and stakeholders in driving sustainable farming strategies globally.

---

## 🎯 Primary Operational Scenarios

### Scenario 1: Smart Crop Recommendation for Farmers
A user inputs localized soil chemical compositions (N, P, K) along with climatic indices (temperature, humidity, pH, rainfall). The internal inference engine analyzes the dataset and instantly predicts the most suitable, high-yield crop for those exact conditions.

### Scenario 2: Crop Suitability and Environmental Assessment
The platform evaluates real-time environmental input parameters against historical crop profiles to determine compatibility thresholds, allowing users to assess whether local conditions match specific crop biological demands.

### Scenario 3: Agricultural Research & Policy Planning
Researchers and policymakers leverage the engine's aggregate analytical intelligence to uncover hidden geographic production patterns, informing environmental policies and global resource optimization.

---

## 🏗️ Technical Architecture & System Requirements

### 💻 System Prerequisites
* **Hardware:** Intel Core i3 Processor or above | Minimum 4 GB RAM | Minimum 10 GB Free Storage Space.
* **Software:** Windows / Linux / macOS | Python 3.x | Anaconda Navigator | Jupyter Notebook | Visual Studio Code.
* **Core Web Architecture:** Built using the **Flask** micro-framework.

### ⚙️ Core Engineering Skills & Toolkits
* **Data Processing & Analytics:** NumPy, Pandas, SciPy.
* **Data Visualization Matrix:** Matplotlib, Seaborn.
* **Predictive Machine Learning Engine:** Scikit-learn.

---

## 🚀 Repository Directory Layout
The project directory is structured as follows:
* `/static` — Contains the high-utility landing page and dashboard background graphic canvases.
* `/templates` — Houses the front-end user interface templates (`home.html`, `about.html`, `findyourcrop.html`).
* `app.py` — The core Flask backend routing manager that processes network forms and runs the ML model.
* `model.pkl` — The serialized trained machine learning predictive pipeline binary file.
* `requirements.txt` — Lists the environment dependencies.

---

## 🛠️ Step-by-Step Execution Guide

### 1. Local Environment Setup
Install the required packages in your local Python environment:
```bash
pip install flask numpy pandas scikit-learn
```

### 2. Launching the Web Application
Open your project inside Visual Studio Code, access your terminal, and run the main entry file:
```bash
python app.py
```

### 3. Interacting with the Live Interface
Click the development link output in your terminal (`http://127.0.0`) to view the application:
* **Home Page (`/`):** Triggers a custom splash intro animation where the white **OPTI CROP** rectangular logo card holds in the center of the viewport before gliding up to the navigation bar.
* **About Page (`/about`):** Displays the technical overview using an asynchronous typewriter text animation over a field backdrop.
* **FindYourCrop Page (`/findyourcrop`):** Contains the 7-parameter environmental input form. Clicking **Predict** immediately displays the live recommended crop (e.g., *coffee*, *cotton*, *chilli*, or *rice*) inside the solid black status footer bar.
