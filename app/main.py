from cutter import full_cutter
from feat_extract_test import extract_feature_test
from csv_sorter import csv_sort
from prediction import predict
from aggregator import aggregator
import pandas as pd
import os
import time

start = time.time()
############### SET ARGS #################

split_length = 30
path = os.getcwd()


## CUT ALL AUDIO SAMPLES INTO 'split_length' SPLITS ###
full_cutter(split_length, path)

# ### EXTRACT AUDIO FEATURES FROM THE SPLITS AND SAVE TO A CSV ###
extract_feature_test(os.path.join(os.getcwd(),"../test_data/myelin_test_split"))


#### SORT CSV FILE ####
csv_sort()


### PREDICT LABELS ###
df = pd.read_csv("myelin_test_features_splitter_sorted.csv")

predict(df)

aggregator("prediction_labels_test.csv")


############################  PREPROCESSING END ########################

end = time.time()

print("Total time from start to end", end-start)