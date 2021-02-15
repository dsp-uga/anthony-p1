import pyspark
import sys
# main entry point for Spark
# SparkContext represents connection to a Spark cluster
spark_conf = pyspark.SparkConf().setMaster("local[*]").setAppName("p0")
sc = pyspark.SparkContext(conf = spark_conf)


if len(sys.argv) != 3:
  raise Exception("Exactly 2 arguments are required: <inputUri> <outputUri>")

inputUri=sys.argv[1]
outputUri=sys.argv[2]


lines = sc.textFile(sys.argv[1])
words = lines.flatMap(lambda line: line.split())
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda count1, count2: count1 + count2)
wordCounts.saveAsTextFile(sys.argv[2])