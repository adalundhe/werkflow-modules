from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_kafka_schema_registry_access_config import LambdaKafkaSchemaRegistryAccessConfig
from .lambda_kafka_schema_validation_config import LambdaKafkaSchemaValidationConfig
from .lambda_schema_registry_event_record_format import LambdaSchemaRegistryEventRecordFormat


class LambdaKafkaSchemaRegistryConfig(BaseModel):
    SchemaRegistryURI: StrictStr | None = None
    EventRecordFormat: LambdaSchemaRegistryEventRecordFormat | None = None
    AccessConfigs: list[LambdaKafkaSchemaRegistryAccessConfig] | None = None
    SchemaValidationConfigs: list[LambdaKafkaSchemaValidationConfig] | None = None
