from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_kafka_schema_registry_config_model import LambdaKafkaSchemaRegistryConfigModel


class LambdaSelfManagedKafkaEventSourceConfigModel(BaseModel):
    ConsumerGroupId: StrictStr | None = None
    SchemaRegistryConfig: LambdaKafkaSchemaRegistryConfigModel | None = None
    ConsumptionMode: StrictStr | None = None
