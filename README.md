anthony-p1
==============================

Project 1: Malware Classification

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   └── model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## Team Member:

Zhongliang Zhou
Shivam Chandan
Nathan Wynn

## GCloud Dataproc Setup Process

- Install Google Cloud SDK
- Set the following environment variables:
    - PROJECT
    - BUCKET_NAME
    - CLUSTER
    - REGION
- Create Dataproc cluster


## Running the Job
`gcloud dataproc jobs submit pyspark <model.py> --cluster=${CLUSTER} --region=${REGION} -- gs://uga-dsp/project1/files gs://anthony-p1-bucket/output`

## Data preprocessing and Feature extraction

X_train.txt, X_train_small.txt, X_test_small.txt and X_test.txt contains names fore the bytes files. By looking at an example of the bytes files, we find that each bytes files contains multiple lines. Starting with an line indicator, each line can be seperated into multiple bicharactor units.

We process each bytes files first to a single line without line indicators and then process it by regarding each two charactors as a word unit. Because hexidecimal combinations, the vocabulary we have would be 256. 

Then, we count each word's apperance based on this vocabulary. And we also removed "??". We further use laplace smoothing by initially set every word count as 1. This would prevent 0 division in naive bayes.

After process, the dataset is transfered into a matrix form of [N, 256]

## Model Training and results

We tested multiple different methods based on the feature matirx generated in the previous step.
|    Models   | Performance  | Discription |
| :----: | :----:  |:----: |
|naive bayes  | 40.51|baseline|
|random forest  | 73.21|without paramters tuning|
| random forest | 95.21 |with paramters tuning|
| GDBT |99.55 | with parameters tuning |

## Autolab Result

score: 98.34619625
ranking: 2
name:Zhou

## Conclusion

In this project, we explore the concepts of Bags of Words model and Naive Bayers. We learned how to perform data prepration on GCP platform

