from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_kafka_schema_registry_config import LambdaKafkaSchemaRegistryConfig


class LambdaAmazonManagedKafkaEventSourceConfig(BaseModel):
    ConsumerGroupId: StrictStr | None = None
    SchemaRegistryConfig: LambdaKafkaSchemaRegistryConfig | None = None
