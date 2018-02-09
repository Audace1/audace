This is a starting kit for the Credit team project proposal "Give me some credit - Sep 19th, 2011".
The dataset contains 150000 examples, 10 features and a binary class to predit. The features give information about the borrower while the class indicates if the load should be granted or not (the borrower will experience financial distress in the next two years or not). The two values that the class can take are not balanced! Indeed, the most of borrowers are considered as trusted ones.

References and credits: This challenge is taken from Kaggle: https://www.kaggle.com/c/GiveMeSomeCredit

Prerequisites: Install Anaconda Python 2.7, including jupyter-notebook

Usage:

(1) If you are a challenge participant:

    The file README.ipynb contains step-by-step instructions on how to create a sample submission for the Iris challenge. At the prompt type: jupyter-notebook README.ipynb

    Download the public_data and replace the sample_data with it.

    Modify sample_code_submission to provide a better model.

    Zip the contents of sample_code_submission (without the directory, but with metadata) to create a submission to the challenge.

    Alternatively, to create a sample result submission run:

    python ingestion_program/ingestion.py public_data sample_result_submission ingestion_program sample_code_submission
	
	python scoring_program/score.py sample_data sample_result_submission scoring_output

    Zip the contents of sample_result_submission (without the directory).

(2) If you are a challenge organizer and use this starting kit as a template, ensure that:

    you modify README.ipynb to provide a good introduction to the problem and good data visualization

    sample_data is a small data subset carved out the challenge TRAINING data, for practice purposes only (do not compromise real validation or test data)

    the following programs run properly (you can substitute sample_xxx_data with any of the 4 kinds of sample data provided):

    python ingestion_program/ingestion.py sample_xxx_data sample_result_submission ingestion_program sample_code_submission

    python scoring_program/score.py sample_xxx_data sample_result_submission scoring_output

    IMPORTANT: if you switch between sample data, remove iris_model.pickle from sample_code_submission, otherwise you'll have inconsistent data and models.

    the metric identified by metric.txt in the utilities directory is the metric used both to compute performances in README.ipynb and for the challenge. To use your own metric, change my_metric.py.

    © 2017 GitHub, Inc.
    Terms
    Pr