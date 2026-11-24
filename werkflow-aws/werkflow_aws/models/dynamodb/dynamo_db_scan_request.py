from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput
from .dynamo_db_condition import DynamoDBCondition
from .dynamo_db_conditional_operator import DynamoDBConditionalOperator
from .dynamo_db_return_consumed_capacity import DynamoDBReturnConsumedCapacity
from .dynamo_db_select import DynamoDBSelect


class DynamoDBScanRequest(BaseModel):
    TableName: StrictStr
    IndexName: StrictStr | None = None
    AttributesToGet: list[StrictStr] | None = None
    Limit: StrictInt | None = None
    Select: DynamoDBSelect | None = None
    ScanFilter: dict[StrictStr, DynamoDBCondition] | None = None
    ConditionalOperator: DynamoDBConditionalOperator | None = None
    ExclusiveStartKey: dict[StrictStr, DynamoDBAttributeValueInput] | None = None
    ReturnConsumedCapacity: DynamoDBReturnConsumedCapacity | None = None
    TotalSegments: StrictInt | None = None
    Segment: StrictInt | None = None
    ProjectionExpression: StrictStr | None = None
    FilterExpression: StrictStr | None = None
    ExpressionAttributeNames: dict[StrictStr, StrictStr] | None = None
    ExpressionAttributeValues: dict[StrictStr, DynamoDBAttributeValueInput] | None = None
    ConsistentRead: StrictBool | None = None
