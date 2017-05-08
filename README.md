# ML-project

Out Kaggle Team tag is "Jarvis (David&Mike)".

## Jupyter Notebooks description:

* check_sumbissions.ipynb: used to compare two submission files generated with 'create_submission.ipynb' and see where are some classifiers performing better than other.
* create_submission.ipynb: this file takes the pandas test dataset and a numpy predictions file and create the final submission .csv file mergind the 'id' of the dataset with the 'bot' column of the predictions.
* feature_extraction.ipynb: this file takes the pandas train dataset (generated with the API using the notebook preproccess_dataset.ipynb) and extract the features used in the algorithms. Refer to the paper to see a list of the features.
* feature_extraction_test.ipynb: same, but for the test dataset.
* new_train_dataset.ipynb: extract features of the new train dataset posted on Kaggle.
* preprocess_dataset.ipynb: takes the original CSV file, extract the usernames, and query all the account information using the Twitter API in batches of 175 accounts. Saves the information in a pandas/numpy/pickle format.
* preprocess_dataset_test.ipynb: same but for the test dataset.
* sentiment_analysis.ipynb: querys the last 200 tweets for each account in the dataset to do some NLP analysis.


In the Final alg folders there are 2 main files: ML_New and ML_New_Norm which hold the main algorithms and their implamentations with and without feature normalization. 

The remaining files are working files. Check those if you feel something is missing.

Please contact us if something is not shown or missing
