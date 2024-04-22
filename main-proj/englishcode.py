import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F



# Set the model to evaluation mode


# Function to predict label and probabilities for user input
def predictType(input_text):

    # Load the fine-tuned DistilBERT model
    model_path = f"C:\\Users\\irfan\\Downloads\\Roberta_sentiment_model_English.pth"
    tokenizer = AutoTokenizer.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment')
    model = AutoModelForSequenceClassification.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment')
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))  # Load the model's state dictionary
    model.eval()

    # Tokenize input text
    inputs = tokenizer(input_text, return_tensors='pt', truncation=True, padding=True)

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)

    # Get predicted label
    predicted_label_idx = torch.argmax(outputs.logits).item()
    predicted_label = model.config.id2label[predicted_label_idx]
    sentiment=['Negative','Neutral','Positive']
    # Get probabilities
    probabilities = F.softmax(outputs.logits, dim=1).squeeze().tolist()

    # print(predicted_label)
    return sentiment[predicted_label_idx]
  
print(predictType("this is good"))