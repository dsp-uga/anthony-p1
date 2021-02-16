import pyspark
import sys
# main entry point for Spark
# SparkContext represents connection to a Spark cluster
spark_conf = pyspark.SparkConf().setMaster("local[*]").setAppName("p0")
sc = pyspark.SparkContext(conf = spark_conf)



def random_forest():
                 '''TODO'''