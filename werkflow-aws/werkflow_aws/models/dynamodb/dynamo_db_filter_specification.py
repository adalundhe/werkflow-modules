from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value_model import DynamoDBAttributeValueModel


class DynamoDBFilterSpecification(BaseModel):
    FilterExpression: StrictStr | None = None
    ProjectionExpression: StrictStr | None = None
    KeyConditionExpression: StrictStr | None = None
    ExpressionAttributeNames: dict[StrictStr, StrictStr] | None = None
    ExpressionAttributeValues: dict[StrictStr, DynamoDBAttributeValueModel] | None = None
