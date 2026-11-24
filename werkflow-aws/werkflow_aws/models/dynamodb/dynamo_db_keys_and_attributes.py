from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput


class DynamoDBKeysAndAttributes(BaseModel):
    Keys: list[dict[StrictStr, DynamoDBAttributeValueInput]]
    AttributesToGet: list[StrictStr] | None = None
    ConsistentRead: StrictBool | None = None
    ProjectionExpression: StrictStr | None = None
    ExpressionAttributeNames: dict[StrictStr, StrictStr] | None = None
