# Sentiment-Analyser-
It is model which can used to predict the sentiment of text

```markdown
# Sentiment Analysis

## Overview

This repository contains a sentiment analysis project implemented in Python using natural language processing (NLP) techniques. The project focuses on classifying text sentiments (Negative, Neutral, Positive) based on a given dataset.

## Project Structure

- `SentimentAnalysis.ipynb`: Jupyter Notebook file containing the code.
- `sentiment_dataset.csv`: Dataset used for training and testing.

## Dependencies

- pandas
- nltk
- scikit-learn

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook:**
   Open and run the `SentimentAnalysis.ipynb` notebook using a tool like Jupyter.

## How it Works

1. **Data Loading:**
   - The dataset is loaded from `sentiment_dataset.csv`.

2. **Text Preprocessing:**
   - Tokenization, lemmatization, and stop-word removal are performed on the text data.

3. **Feature Extraction:**
   - TF-IDF vectorization is used to convert text data into numerical features.

4. **Model Training:**
   - The Multinomial Naive Bayes classifier is trained on the preprocessed data.

5. **Model Evaluation:**
   - The model is evaluated on a test set, and accuracy and classification reports are displayed.

## Results

The model achieves an accuracy of ' ' on the test set. See the `classification_report` for detailed performance metrics.

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Your feedback is highly appreciated!
