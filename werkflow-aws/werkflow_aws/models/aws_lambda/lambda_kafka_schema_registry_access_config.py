from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_kafka_schema_registry_auth_type import LambdaKafkaSchemaRegistryAuthType


class LambdaKafkaSchemaRegistryAccessConfig(BaseModel):
    Type: LambdaKafkaSchemaRegistryAuthType | None = None
    URI: StrictStr | None = None
