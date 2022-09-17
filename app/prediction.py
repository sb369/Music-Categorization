import imp
import pandas as pd
from tensorflow import keras
import sklearn.preprocessing as skp
from joblib import load


def language(x_df):
    index_label = {0: 'tamil', 1: 'telugu', 2: 'malayalam', 3: 'bengali', 4: 'english', 5: 'kannada', 6: 'hindi', 7: 'marathi'}
    model = keras.models.load_model("models/v1_language_model.h5")
    print(model.summary())
    x = x_df.iloc[:,2:]
#     print(x)
    scaler = load('models/std_scaler.bin')
    x = pd.DataFrame(scaler.transform(x), columns=x.columns)
#     print(x)
#     x=x_df
    y_prob = model.predict(x)
    print("lang preds:")
    print(y_prob)
    pred_labels = y_prob.argmax(axis=-1)
    
    pred = []
    for p in pred_labels:
        pred.append(index_label[p])
    return pred

def label(x_df):
    index_label = {0: 'party', 1: 'motivational', 2: 'adventure', 3: 'relax', 4: 'family'}
    model = keras.models.load_model("models/v1_label_model.h5")
    print(model.summary())
    x = x_df.iloc[:,2:]
#     print(x)
    scaler = load('models/std_scaler.bin')
    x = pd.DataFrame(scaler.transform(x), columns=x.columns)
#     print(x)
#     x=x_df
    y_prob = model.predict(x)
    print("label preds")
    print(y_prob)
    pred_labels = y_prob.argmax(axis=-1)
    
    pred = []
    for p in pred_labels:
        pred.append(index_label[p])
    return pred

def predict(x_df):
    lang = language(x_df)
    lab = label(x_df)
    pred = pd.DataFrame()
    pred["song_name"] = x_df["song_name"]
    pred["language"] = lang
    pred["label"] = lab
    pred.to_csv("prediction_labels_test.csv")
    print(pred)
    return pred

# df = pd.read_csv("myelin_test_features_splitter_sorted.csv")

# predict(df)