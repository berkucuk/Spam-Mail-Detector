import torch
from transformers import AutoTokenizer, BertModel
from torch import nn
import numpy as np

# Load the model
class Model(nn.Module):
    def __init__(self, num_labels=2):
        super().__init__()
        self.bert = BertModel.from_pretrained("bert-base-uncased")
        self.batchnorm = nn.BatchNorm1d(self.bert.config.hidden_size)
        self.fc3 = nn.Linear(self.bert.config.hidden_size, num_labels)

    def forward(self, input_ids, attention_mask):
        bert_outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        bert_embds = bert_outputs.pooler_output
        x = self.batchnorm(bert_embds)
        logits = self.fc3(x)
        return logits

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Model().to(device)

# Load trained weights
model.load_state_dict(torch.load('model.pth', map_location=device))
model.eval()

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Function to clean and tokenize input text
def tokenizer_text(text):
    t = tokenizer.encode_plus(text, max_length=64,
                              truncation=True,
                              padding='max_length',
                              add_special_tokens=True,
                              return_tensors='pt')
    return t

# Prediction function
def predict(text, model):
    tokens = tokenizer_text(text)
    input_ids = tokens['input_ids'].to(device)
    attention_mask = tokens['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask)
        _, predicted = torch.max(outputs, 1)

    return "Spam" if predicted.item() == 1 else "Not Spam"

# Get input from the terminal and make a prediction
if __name__ == "__main__":
    input_text = input("Enter the message to classify: ")
    prediction = predict(input_text, model)
    print(f"The message is: {prediction}")
