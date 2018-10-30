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
-------- | -----------
m<sup>a</sup> | Memory usage when Apache Spark operate action
m<sup>t</sup> | Memory usage when Apache Spark operate transformation
c<sup>u</sup> | CPU usage of user processed
c<sup>s</sup> | CPU usage of system processed
b<sup>i</sup> | Network usage of inbound network to master node
b<sup>o</sup> | Network usage of outbound network from master node
x             | The current number of worker nodes in cluster
y             | The scaling number of worker nodes
A<sup>i</sup><sub>y</sub> | Action to scale in with y worker nodes
A<sup>o</sup><sub>y</sub> | Action to scale out with y worker nodes

### There are 2 Docker containers
* [Docker container on Apache Spark cluster](https://hub.docker.com/r/kundjanasith/kitwai_engine/)
* [Docker container on Cluster management node](https://hub.docker.com/r/kundjanasith/kitwai_webui/)