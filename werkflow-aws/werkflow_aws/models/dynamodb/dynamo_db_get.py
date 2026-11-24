from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput


class DynamoDBGet(BaseModel):
    Key: dict[StrictStr, DynamoDBAttributeValueInput]
    TableName: StrictStr
    ProjectionExpression: StrictStr | None = None
    ExpressionAttributeNames: dict[StrictStr, StrictStr] | None = None
