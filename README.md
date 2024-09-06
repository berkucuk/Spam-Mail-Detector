
# Spam Email Classifier

## Project Overview

This project is designed to classify emails as either **"Spam"** or **"Not Spam"** using a deep learning model based on BERT (Bidirectional Encoder Representations from Transformers). The model processes input email text and predicts whether the email is spam or not.

## Features

- **Data Cleaning**: The email content is preprocessed, including converting text to lowercase, removing punctuation, stopwords, and applying lemmatization to extract word roots.
- **BERT Model**: Uses a pre-trained BERT model to convert email text into meaningful vector representations.
- **Cross-validation**: Splits the dataset into training, validation, and testing sets to evaluate the model's performance.
- **Visualization**: Displays the model's performance using a confusion matrix.

## Project Contents

- `model.pth`: Trained model weights.
- `train_model`: Code for training the model.
- `test_model`: Code for testing and evaluating the model.
- `predict`: Function to predict whether an email is spam or not based on user input.
- `confusion_matrix`: Visualization of test results through a confusion matrix.

## Setup

To run this project, follow these steps:

1. **Install Requirements**:

   Run the following command to install the required Python libraries:

   ```bash
   pip install torch torchvision transformers scikit-learn matplotlib pandas numpy
   ```

2. **Download Dataset and Model**:

   Download the dataset from Kaggle using the following commands:

   ```bash
   kaggle datasets download -d devildyno/email-spam-or-not-classification
   unzip email-spam-or-not-classification.zip
   ```

3. **Train the Model (Optional)**:

   If you want to train the model from scratch, use the `train_model` function. The trained model will be saved as `model.pth`.

4. **Run the Classifier**:

   After the model is trained and saved, run the following command to make predictions from the terminal:

   ```bash
   python3 spam_email_classifier.py
   ```

   You will be prompted to enter an email message, and the model will classify it as "Spam" or "Not Spam."

## Usage

1. **Training the Model**:

   To train the model, after downloading the dataset, call the `train_model` function. The model will be trained for 4 epochs, and the weights will be saved in `model.pth`.

2. **Predicting Spam/Not Spam**:

   To classify an email, run the classifier, and you'll see the following prompt in the terminal:

   ```
   Enter the message to classify: 
   ```

   Enter your email content, and the model will predict whether it's **"Spam"** or **"Not Spam"**.

## Example Usage

```bash
Enter the message to classify: You have won a $1000 gift card! Click here to claim your prize.
The message is: Spam
```

```bash
Enter the message to classify: Meeting is scheduled for 10 AM tomorrow. Please be on time.
The message is: Not Spam
```

## Model Performance

The model's performance was evaluated on a test dataset, and a confusion matrix is used to visualize the results. The model achieves over 90% accuracy in classifying emails as spam or not.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

This `README.md` file explains the project's purpose, how it works, and how to set it up for use. You can include this in your GitHub repository to guide users.
