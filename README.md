## Q1:How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
Playing around with different config values impacted `inputRowsPerSecond` and `processedRowsPerSecond`. Based on different parameters sometimes both throughput and delay increased


## Q2: What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

In my experimentation, when using the default values I get about 60 `processedRowsPerSecond`, but when especially increased `maxOffsetPerTrigger` to 5K then I got a better throughput of `processedRowsPerSecond : 352.85815102328866`

I also played with other params such as 
 - `maxRatePerPartition`
 - `spark.sql.inMemoryColumnarStorage.batchSize`
 - `spark.sql.shuffle.partitions`

However they were not impacting the throghput/delay drastically

