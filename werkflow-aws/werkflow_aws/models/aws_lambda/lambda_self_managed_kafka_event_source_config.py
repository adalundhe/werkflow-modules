from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_kafka_event_source_mapping_consumption_mode import LambdaKafkaEventSourceMappingConsumptionMode
from .lambda_kafka_schema_registry_config import LambdaKafkaSchemaRegistryConfig


class LambdaSelfManagedKafkaEventSourceConfig(BaseModel):
    ConsumerGroupId: StrictStr | None = None
    SchemaRegistryConfig: LambdaKafkaSchemaRegistryConfig | None = None
    ConsumptionMode: LambdaKafkaEventSourceMappingConsumptionMode | None = None
