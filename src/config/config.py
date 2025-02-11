config = {
    "openai": {
        "api_key": "OPENAI_API"
    },
    "kafka": {
        "sasl.username": "KAFKA_CLUSTER_USERNAME",
        "sasl.password": "KAFKA_CLUSTER_PASSWORD",
        "bootstrap.servers": "SERVER_URL",
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'PLAIN',
        'session.timeout.ms': 50000
    },
    "schema_registry": {
        "url": "SCHEMA_REGISTRY_URL",
        "basic.auth.user.info": "SCHEMAAPI_USERNAME:SCHEMAAPI_PASSWORD"

    }
}
