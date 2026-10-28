
# 💬 AI-Powered Sentiment Analysis

An AI-Powered Sentiment Analysis application that classifies customer reviews into three sentiment categories: **Positive, Negative, and Neutral**.

This project uses Natural Language Processing (NLP) and traditional Machine Learning algorithms to process text reviews, compare feature extraction techniques, evaluate model performance, and provide predictions through an interactive Streamlit web application.

## 🚀 Features

- Three-class sentiment classification: Positive, Negative, and Neutral.
- Text feature extraction using TF-IDF and Bag of Words (BoW).
- Comparison of Logistic Regression and Multinomial Naive Bayes.
- Training and evaluation of four Machine Learning pipelines.
- Five-fold cross-validation.
- Hyperparameter tuning using GridSearchCV.
- Evaluation using Accuracy, Precision, Recall, and F1-score.
- Classification reports and confusion matrix visualization.
- Model serialization using Joblib.
- Interactive Streamlit web application.
- Class probability visualization when supported by the selected model.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Dataset handling and analysis |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning and evaluation |
| TF-IDF | Text feature extraction |
| Bag of Words | Text representation |
| Logistic Regression | Sentiment classification |
| Multinomial Naive Bayes | Sentiment classification |
| Matplotlib | Evaluation visualizations |
| Seaborn | Confusion matrix visualization |
| Joblib | Saving and loading the trained pipeline |
| Streamlit | Interactive web interface |
| Google Colab | Model development and experimentation |
| VS Code | Application development |

## 📂 Dataset

The dataset contains **10,000 customer review records** and five columns.

| Column | Description |
|---|---|
| `review_id` | Unique review identifier |
| `review_text` | Text of the customer review |
| `sentiment` | Sentiment label |
| `category` | Review category |
| `source` | Source of the review |

### Dataset inspection

The notebook's data inspection shows:

- Total records: 10,000
- Total columns: 5
- Missing values: None reported
- Duplicate records: None reported
- Sentiment classes: Positive, Negative, Neutral

The sentiment distribution visualization shows approximately balanced representation across the three classes.

## 🧠 Machine Learning Workflow

### 1. Data Exploration

- Inspected the dataset using Pandas.
- Examined column types and descriptive statistics.
- Checked for missing values and duplicate records.
- Visualized the distribution of sentiment classes.

### 2. Data Preparation

The dataset was divided into training and testing sets.

| Dataset | Records |
|---|---:|
| Training set | 8,000 |
| Testing set | 2,000 |
| Total | 10,000 |

### 3. Text Feature Extraction

Two text vectorization approaches were compared.

**TF-IDF (Term Frequency–Inverse Document Frequency)**

Assigns weights to words based on their importance within a document relative to the collection of documents.

**Bag of Words (BoW)**

Represents text using word occurrence or frequency features without considering word order.

### 4. Model Training

Four combinations of feature extraction and classification algorithms were evaluated.

| Model | Feature Extraction | Classifier |
|---|---|---|
| Model 1 | TF-IDF | Logistic Regression |
| Model 2 | TF-IDF | Multinomial Naive Bayes |
| Model 3 | Bag of Words | Logistic Regression |
| Model 4 | Bag of Words | Multinomial Naive Bayes |

### 5. Cross-Validation and Hyperparameter Tuning

Five-fold cross-validation and GridSearchCV were used to compare candidate configurations.

The notebook evaluated 12 parameter candidates per model, resulting in 60 cross-validation fits per model and 240 fits across all four configurations.

The reported selection criterion was **Macro F1-score**, which gives equal importance to each sentiment class.

The notebook selected TF-IDF with Logistic Regression as the best model, reporting a cross-validation Macro F1-score of 1.00.

## 📊 Model Evaluation Results

### Reported test-set performance

The notebook reports the following results on the 2,000-record test set.

| Model | Accuracy | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| TF-IDF + Logistic Regression | 1.00 | 1.00 | 1.00 | 1.00 |
| TF-IDF + Naive Bayes | 1.00 | 1.00 | 1.00 | 1.00 |
| BoW + Logistic Regression | 1.00 | 1.00 | 1.00 | 1.00 |
| BoW + Naive Bayes | 1.00 | 1.00 | 1.00 | 1.00 |

These are the values reported by the current notebook, not independently verified performance estimates.

### Selected model

**TF-IDF + Logistic Regression**

The notebook selected this pipeline based on its reported cross-validation Macro F1-score.

The displayed classification report gives the following support:

| Sentiment | Test records | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|
| Negative | 667 | 1.00 | 1.00 | 1.00 |
| Neutral | 666 | 1.00 | 1.00 | 1.00 |
| Positive | 667 | 1.00 | 1.00 | 1.00 |

The displayed confusion matrix contains only diagonal values, with no errors reported.

### Evaluation caution

Perfect scores across all four models can indicate a very easy dataset, duplicated or overlapping records, sentiment labels encoded in the review text, or another form of data leakage.

Before treating these metrics as evidence of real-world performance:

- Check whether review text directly reveals the sentiment label.
- Check for duplicates and near-duplicates across the train/test split.
- Confirm that the test set was not used for fitting or model selection.
- Inspect the dataset's source and label-generation procedure.
- Test on independent, realistic reviews that were not used during development.

The results should be re-evaluated if these checks reveal leakage.

## 📁 Project Structure

A suggested repository structure is:

```text
ai-powered-sentiment-analysis/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── sentiment_analysis.pkl
│
├── notebooks/
│   └── sentiment_analysis.ipynb
│
└── reports/
    ├── classification_report.json
    ├── cross_validation_results.csv
    └── evaluation_plots/
```

Update the structure to match the actual files included in your repository.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-powered-sentiment-analysis.git
cd ai-powered-sentiment-analysis
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Place the trained model

Ensure the trained pipeline is saved at:

```text
models/sentiment_analysis.pkl
```

The path and filename in `app.py` must match the location of the saved model.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local address displayed in the terminal, usually:

```text
http://localhost:8501
```

## 💻 Using the Application

1. Open the Sentiment AI application in your browser.
2. Enter a customer review in the text input area.
3. Click **Analyze Sentiment**.
4. View the predicted sentiment.
5. Inspect class probability estimates if the pipeline supports them.

### Example reviews

| Review | Expected sentiment |
|---|---|
| The product is excellent and works perfectly. | Positive |
| The quality is terrible and I am disappointed. | Negative |
| The package arrived yesterday. | Neutral |

These are illustrative examples. Actual predictions depend on the trained model.

## 💾 Saving the Model

The selected pipeline can be serialized using Joblib:

```python
import joblib

joblib.dump(
    best_model,
    "sentiment_analysis.pkl"
)
```

Load the pipeline in the application:

```python
import joblib

model = joblib.load("sentiment_analysis.pkl")
```

Saving the complete pipeline preserves the vectorizer and classifier together, allowing raw review text to be passed directly to the prediction method.

Use compatible Python and Scikit-learn versions when saving and loading the model.

## 🔮 Future Improvements

- Validate performance on an independent external dataset.
- Add batch sentiment prediction from CSV files.
- Allow users to download prediction results.
- Add interactive sentiment distribution charts.
- Improve handling of sarcasm, negation, and ambiguous reviews.
- Compare against additional NLP models.
- Deploy the application to a public hosting platform.

## ⚠️ Limitations

- Predictions depend on the dataset and the model's training quality.
- Sarcasm and context-dependent expressions may be difficult to classify.
- Probability estimates are not guarantees of correctness.
- Reported perfect evaluation scores require further validation.
- The application is intended for educational and analytical purposes.

## 👨‍💻 Author

**Sunny Rai**

BCA — Artificial Intelligence and Machine Learning

