from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput
from .dynamo_db_return_consumed_capacity import DynamoDBReturnConsumedCapacity


class DynamoDBGetItemRequest(BaseModel):
    TableName: StrictStr
    Key: dict[StrictStr, DynamoDBAttributeValueInput]
    AttributesToGet: list[StrictStr] | None = None
    ConsistentRead: StrictBool | None = None
    ReturnConsumedCapacity: DynamoDBReturnConsumedCapacity | None = None
    ProjectionExpression: StrictStr | None = None
    ExpressionAttributeNames: dict[StrictStr, StrictStr] | None = None
