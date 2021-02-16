import pyspark

# main entry point for Spark
# SparkContext represents connection to a Spark cluster
spark_conf = pyspark.SparkConf().setMaster("local[*]").setAppName("p0")
sc = pyspark.SparkContext(conf = spark_conf)



# TODO
# 1. Preprocessing (bag of words, feature set)
# 2. Naive Bayes
# 3. Work on other models

def preprocess():
               '''TODO'''

def naive_bayes():
               ''' TODO'''

def random_forest():
                 '''TODO'''