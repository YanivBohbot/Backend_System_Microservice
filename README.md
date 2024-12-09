# Backend_System_Microservice

Overview

This project is a modular and scalable backend system designed with a microservices architecture. Each microservice is responsible for a specific business function, and Apache Kafka is used for event-driven communication between them. The system ensures seamless handling of orders, processing workflows, notifications, and analytics.
Architecture
Microservices

    Order Service
        Role: Producer
        Description: This service handles the creation of new orders. It publishes order events to a Kafka topic for other services to consume.
        Kafka Topic(s):
            order-created: Published when a new order is created.

    Order Processing Service
        Role: Consumer & Producer
        Description: This service processes incoming orders by consuming events from the order-created topic. Once processed, it publishes status updates to a Kafka topic for further actions.
        Kafka Topic(s):
            Consumes: order-created
            Produces: order-processed

    Notification Service
        Role: Consumer
        Description: This service listens to events from the order-processed topic and sends notifications to customers about their order status.
        Kafka Topic(s):
            Consumes: order-processed

    Analytics Service
        Role: Consumer
        Description: This service aggregates and analyzes order and processing data by consuming messages from multiple Kafka topics. It generates insights and visualizations for the system.
        Kafka Topic(s):
            Consumes: order-created, order-processed
