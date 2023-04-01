from simpletransformers.classification import (
    MultiLabelClassificationModel,
    MultiLabelClassificationArgs,
)
import pickle
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

# Load the test dataset
test_df = pd.read_pickle("test_df")

# Load the pre-trained multi-label classification model
model = MultiLabelClassificationModel(
    "roberta", "D:/jupyter/bd2/project/outputs/checkpoint-1001490-epoch-42"
)

# Load the MultiLabelBinarizer used to decode the labels in the dataset
mlb = pickle.load(open("mlb.pkl", "rb"))


# Define a function to get the top 10 predicted labels
def get_top_10_preds(output):
    indices = sorted(range(len(output)), key=lambda i: output[i], reverse=True)[:10]
    return mlb.classes_[indices]


# Define a function to recommend products for a given user
def recommend_products(user_index):
    # Make predictions on the text of the given user using the pre-trained model
    _, raw_outputs = model.predict([test_df["text"][user_index]])
    cur_prod = mlb.inverse_transform(test_df["labels"][user_index].reshape(1, 1000))[0]
    prev_prods = test_df["text"][user_index]
    rec_prods = get_top_10_preds(raw_outputs[0])
    return cur_prod, prev_prods, rec_prods
