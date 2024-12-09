# 🚀 **Backend System with Microservices**

## 📜 **Overview**
This project is a modular and scalable **backend system** built using **microservices** architecture. Each microservice is responsible for a distinct business function, and **Apache Kafka** is utilized as the communication backbone for seamless **event-driven communication**.

The system consists of four main microservices:
- **Order Service** (Producer)
- **Order Processing Service** (Consumer & Producer)
- **Notification Service** (Consumer)
- **Analytics Service** (Consumer)

These services interact asynchronously through **Kafka topics**, ensuring a **decoupled**, **scalable**, and **fault-tolerant** system.

---

## 🏗️ **Architecture**

### Microservices Overview
Below is the breakdown of each microservice in the system:

1. ### 🛒 **Order Service**
   - **Role**: Producer  
   - **Description**: Handles creation of new orders and publishes order events to a Kafka topic.
   - **Kafka Topic(s)**:
     - `order-created`

2. ### ⚙️ **Order Processing Service**
   - **Role**: Consumer & Producer  
   - **Description**: Processes incoming orders by consuming events from `order-created`. Upon processing, publishes status updates to `order-processed`.
   - **Kafka Topic(s)**:
     - Consumes: `order-created`
     - Produces: `order-processed`

3. ### 🔔 **Notification Service**
   - **Role**: Consumer  
   - **Description**: Listens to the `order-processed` topic to notify users in real-time about the status of their order.
   - **Kafka Topic(s)**:
     - Consumes: `order-processed`

4. ### 📊 **Analytics Service**
   - **Role**: Consumer  
   - **Description**: Aggregates and analyzes data by consuming messages from multiple Kafka topics (`order-created`, `order-processed`) for reporting and insights.
   - **Kafka Topic(s)**:
     - Consumes: `order-created`, `order-processed`

---

## 🛠️ **Apache Kafka Communication**

### Topics Overview
The communication between microservices uses **Kafka topics**:

- **`order-created`**: Sent by the **Order Service** to notify other services of newly created orders.
- **`order-processed`**: Sent by the **Order Processing Service** once an order has been successfully processed.

### Event Flow
1. **Order Service** publishes events to `order-created`.
2. **Order Processing Service** consumes these events, processes them, and then publishes an event to `order-processed`.
3. The **Notification Service** and **Analytics Service** consume messages from `order-processed` or other relevant topics.

---

## 💡 **Key Features**

✅ **Event-Driven Architecture**: Designed with Kafka for asynchronous communication.  
✅ **Modular Design**: Independent microservices can scale or be updated independently.  
✅ **Real-Time Notifications**: Automated notifications sent to users about order status.  
✅ **Data-Driven Insights**: Analytics service provides insights using order processing data.  
✅ **Fault Tolerance**: Kafka ensures that service failures don't break communication workflows.

---

## 💻 **Technology Stack**

- **Programming Language**: Python
- **Messaging System**: Apache Kafka
- **Database**: not choose yet -> e.g., PostgreSQL, MongoDB, MySQL)
- **Web Framework**: not choose yet -> e.g., Flask, FastAPI, Express
- **Other Tools/Dependencies**: List additional frameworks/libraries.

---

## 🚀 **Setup & Installation**

### 1. Clone the Repository
```bash
git clone https://github.com/YanivBohbot/Backend_System_Microservice.git
cd Backend_System_Microservice


### 2.  Install Dependencies
```bash
# Example for Python
pip install -r requirements.txt


### 3.  Set up Kafka
```bash
kafka-topics.sh --create --topic order-created --bootstrap-server localhost:9092
kafka-topics.sh --create --topic order-processed --bootstrap-server localhost:9092


### 4. Configure Environment Variables

#Update configuration files or .env with the necessary Kafka settings and service configurations.
```bash
# Example for Python
pip install -r requirements.txt


### 5. Start Microservices

#Update configuration files or .env with the necessary Kafka settings and service configurations.
```bash
python order_service.py
python processing_service.py
python notification_service.py
python analytics_service.py












