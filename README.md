## To Optimize an Auto-Scaling on Apache Spark using Deep Reinforcement Learning

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

### Features
No. | Feature | Description
--- | ------- | -----------
01 | SparkContext | Apache Spark framework metadata
02 | SecurityManager | Authentication & Permission 
03 | Utils | SparkDriver port 
04 | SparkEnv | Register directory
05 | BlockManagerMasterEndpoint | Register block
06 | DiskBlockManager | Create local /tmp
07 | MemoryStore | Memory usage when Apache Spark operate action
08 | Log | Initial Apache Spark Logging
09 | Server | Apache Spark server [ jetty ]
10 | AbstractConnector | Start Server Connector
11 | ContextHandler | Apache Spark job state
12 | SparkUI | Spark UI URL
13 | StandaloneAppClient | Master node URL
14 | TransportClient | Master node connection
15 | StandaloneScheduler | RegisteredResourcesRatio scheduler 
16 | NettyBlockTransferService | Initial Netty service
17 | BlockManager | Initial Resilient Distributed Datasets
18 | BlockManagerMaster | Register BlockManager ID
19 | EventLoggingListener | Create server /tmp
20 | BlockManagerInfo | Memory usage when Apache Spark operate transformation
21 | FileInputFormat | Input file path and format
22 | CoarseGrainedSchedulerBackend | Netty endpoint reference
23 | DAGScheduler | DAG stage
24 | TaskSchedulerImpl | Schedule resources pool to tasks
25 | TaskSetManager | Manage task set on job scheduler
26 | MapOutputTrackerMasterEndpoint | Request and response between Map & Reduce
27 | MapOutputTrackerMaster | Size of output status
28 | TransportClientFactory | Execution URL stage
29 | ApplicationName | Application information
30 | TorrentBroadcast | Destroying replicated broadcast
31 | MapPartitionsRDD | Removing Resilient Distributed Datasets
32 | ContextCleaner | Cleaned context when shuffle and RDD
33 | OutputCommitCoordinator | Commit output stage 
34 | ShutdownHookManager | Deleting sever /tmp


### There are 2 Docker containers
* [Docker container on Apache Spark cluster](https://hub.docker.com/r/kundjanasith/kitwai_engine/)
* [Docker container on Cluster management node](https://hub.docker.com/r/kundjanasith/kitwai_webui/)
