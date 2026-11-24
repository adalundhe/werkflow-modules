from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput
from .dynamo_db_return_values_on_condition_check_failure import DynamoDBReturnValuesOnConditionCheckFailure


class DynamoDBUpdate(BaseModel):
    Key: dict[StrictStr, DynamoDBAttributeValueInput]
    UpdateExpression: StrictStr
    TableName: StrictStr
    ConditionExpression: StrictStr | None = None
    ExpressionAttributeNames: dict[StrictStr, StrictStr] | None = None
    ExpressionAttributeValues: dict[StrictStr, DynamoDBAttributeValueInput] | None = None
    ReturnValuesOnConditionCheckFailure: DynamoDBReturnValuesOnConditionCheckFailure | None = None
