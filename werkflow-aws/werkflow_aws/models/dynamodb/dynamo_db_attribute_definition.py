from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_scalar_attribute_type import DynamoDBScalarAttributeType


class DynamoDBAttributeDefinition(BaseModel):
    AttributeName: StrictStr
    AttributeType: DynamoDBScalarAttributeType
