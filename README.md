## Auto-Scaling on Apache Spark using Deep Reinforcement Learning

### Directory structure
```
--|-- dqn_agent.py                          # Deep Q-Network agent
  |-- model.py                              # Deep Reinforcement Learning model application
  |-- server.py                             # Monitor Deep Reinforcement Learning model server
  |-- spark_cluster.py                      # Deep Q-Network environment on Apache Spark cluster
  |-- test.py                               # Deep Reinforcement Learning model inference
  |-- train.py                              # Deep Reinforcement Learning model training
  |-- train_set.sh                          # Training set script with constraints
  |-- kitwai-models                         # Pre-trained model
      |-- checkpoint
      |-- spark.data-00000-of-00001
      |-- spark.index
      |-- spark.meta
```
### System Architecture
![System Architecture](/images/system_engine.png)
Variable | Description
------------ | -------------
m<sup>a</sup> | Memory usage when Apache Spark operate action
Content column 1 | Content column 2

### There are 2 Docker containers
* [Docker container on Apache Spark cluster](https://hub.docker.com/r/kundjanasith/kitwai_engine/)
* [Docker container on Cluster management node](https://hub.docker.com/r/kundjanasith/kitwai_webui/)