import pyspark
import sys

# import urllib.request as read_file

# main entry point for Spark
# SparkContext represents connection to a Spark cluster
spark_conf = pyspark.SparkConf().setMaster("local[*]").setAppName("p0")
sc = pyspark.SparkContext(conf = spark_conf)


if len(sys.argv) != 3:
  raise Exception("Exactly 2 arguments are required: <inputUri> <outputUri>")

inputUri=sys.argv[1]
outputUri=sys.argv[2]


lines = sc.textFile(sys.argv[1])

# Call collect() to get all data
llist = lines.collect()

# generate dictionary
hexidecimal_list = "0123456789ABCDEF"
dictionary = {}
# ignore list: stop words
ignore_list = ["??"]

for i in hexidecimal_list:
  for j in hexidecimal_list:
      dictionary.update({i+j: 1})


for line in llist:
    # make a copy of dictionary
    dictionary_tmp = dictionary
    # read bytes file
    binaryPath='gs://uga-dsp/project1/data/bytes/'+line.strip()+'.bytes'
    bytesfile = sc.textFile(binaryPath)
    content = bytesfile.collect()
    # read lines
    for item in content:
        item = item.split(" ")[1:]
        for charactor in item:
          if charactor not in ignore_list:
            # update dictionary
            dictionary_tmp[charactor] += 1
    rdd = sc.parallelize([dictionary_tmp])
    rdd.repartition(1).saveAsTextFile(sys.argv[2]+"/"+line)




