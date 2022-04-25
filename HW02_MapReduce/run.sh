#!/usr/bin/env bash
set -x

HADOOP_STREAMING_JAR=/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar
NUM_REDUCERS=3

hdfs dfs -rm -r -skipTrash ${2}

yarn jar $HADOOP_STREAMING_JAR \
    -D mapred.job.name="$3"\
    -files "mapper.py,reducer.py" \
    -mapper "./mapper.py" \
    -reducer "./reducer.py" \
    -numReduceTasks 2 \
    -input "$1/*" \
    -output "$2" \

hdfs dfs -cat "$2/*" | head -n 50 > "hw02_mr_data_ids.out"
cat "hw02_mr_data_ids.out" | head -n 50