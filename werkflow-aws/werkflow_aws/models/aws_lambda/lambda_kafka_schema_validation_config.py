from __future__ import annotations
from pydantic import BaseModel
from .lambda_kafka_schema_validation_attribute import LambdaKafkaSchemaValidationAttribute


class LambdaKafkaSchemaValidationConfig(BaseModel):
    Attribute: LambdaKafkaSchemaValidationAttribute | None = None
