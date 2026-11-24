from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_kafka_schema_registry_access_config_model import LambdaKafkaSchemaRegistryAccessConfigModel
from .lambda_kafka_schema_validation_config_model import LambdaKafkaSchemaValidationConfigModel


class LambdaKafkaSchemaRegistryConfigModel(BaseModel):
    SchemaRegistryURI: StrictStr | None = None
    EventRecordFormat: StrictStr | None = None
    AccessConfigs: list[LambdaKafkaSchemaRegistryAccessConfigModel] | None = None
    SchemaValidationConfigs: list[LambdaKafkaSchemaValidationConfigModel] | None = None
