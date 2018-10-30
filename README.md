# Auto-scaling on Apache Spark using Deep Reinforcement Learning

## Directory structure
```
--|
  |-- dqn_agent.py
  |-- model.py 
  |-- server.py
  |-- spark_cluster.py
  |-- test.py
  |-- train.py
  |-- train_set.sh
  |-- kitwai-models
      |-- checkpoint
      |-- spark.data-00000-of-00001
      |-- spark.index
      |-- spark.meta
```

## There are 2 Docker containers
* [Docker container on Apache Spark cluster](https://hub.docker.com/r/kundjanasith/kitwai_engine/)
* [Docker container on Cluster management node](https://hub.docker.com/r/kundjanasith/kitwai_webui/)