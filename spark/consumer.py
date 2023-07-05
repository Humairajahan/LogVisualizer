from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, StringType, LongType, TimestampType


jdbc_url = "jdbc:postgresql://db:5432/logs"
jdbc_table = "log-data"
jdbc_properties = {
    "user": "username",
    "password": "password"
}

KAFKA_BOOTSTRAP_SERVERS = "PLAINTEXT://kafka:29092"
KAFKA_TOPIC = "MSGS"

SCHEMA = StructType([
    StructField("TIME", TimestampType()),
    StructField("LEVEL", StringType()),
    StructField("MESSAGE", LongType())
])


spark = SparkSession.builder.appName("consumer").getOrCreate()
spark.sparkContext.setLogLevel("DEBUG")

df = spark\
    .readStream.format("kafka")\
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS)\
    .option("subscribe", KAFKA_TOPIC)\
    .option("startingOffsets", "earliest")\
    .load()

def process_incoimng_msg(data):
    sections = data.split(":", 2)
    if len(sections) == 3:
        return {
            "TIME": F.to_timestamp(sections[0].strip()),
            "LEVEL": sections[1].strip(),
            "MESSAGE": sections[2].strip()
        }
    else:
        pass

processed_df = df.select(
    F.col("value").cast("string").alias("value")
) \
.withColumn("processed", F.from_json(F.col("value"), SCHEMA)) \
.select("processed.*")
    
processed_df = processed_df.withColumn("MESSAGE", F.trim(F.col("MESSAGE")))

print("---------------------- Dataframe after processing -------------")
processed_df.show()

processed_df.write \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", jdbc_table) \
    .option("user", jdbc_properties["user"]) \
    .option("password", jdbc_properties["password"]) \
    .mode("append") \
    .save()
