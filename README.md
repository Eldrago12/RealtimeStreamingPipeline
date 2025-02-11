# Realtime Data Streaming With TCP Socket, Apache Spark, Kafka, OpenAI API and Elasticsearch

The project is designed with the following components:

- Data Source: We use yelp.com dataset for our pipeline.
- TCP/IP Socket: Used to stream data over the network in chunks
- Apache Spark: For data processing with its master and worker nodes.
= Confluent Kafka: Our cluster on the cloud
- Control Center and Schema Registry: Helps in monitoring and schema management of our Kafka streams.
- Kafka Connect: For connecting to elasticsearch
- Elasticsearch: For indexing and querying

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Eldrago12/RealtimeStreamingPipeline.git
   ```

2. Navigate to the project directory:
  ```bash
  cd RealtimeStreamingPipeline
  ```

3. To spin up the cluster:
   ```bash
   docker-compose up
   ```
