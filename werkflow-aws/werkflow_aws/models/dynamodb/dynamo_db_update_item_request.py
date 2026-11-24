from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput
from .dynamo_db_attribute_value_update import DynamoDBAttributeValueUpdate
from .dynamo_db_conditional_operator import DynamoDBConditionalOperator
from .dynamo_db_expected_attribute_value import DynamoDBExpectedAttributeValue
from .dynamo_db_return_consumed_capacity import DynamoDBReturnConsumedCapacity
from .dynamo_db_return_item_collection_metrics import DynamoDBReturnItemCollectionMetrics
from .dynamo_db_return_value import DynamoDBReturnValue
from .dynamo_db_return_values_on_condition_check_failure import DynamoDBReturnValuesOnConditionCheckFailure


class DynamoDBUpdateItemRequest(BaseModel):
    TableName: StrictStr
    Key: dict[StrictStr, DynamoDBAttributeValueInput]
    AttributeUpdates: dict[StrictStr, DynamoDBAttributeValueUpdate] | None = None
    Expected: dict[StrictStr, DynamoDBExpectedAttributeValue] | None = None
    ConditionalOperator: DynamoDBConditionalOperator | None = None
    ReturnValues: DynamoDBReturnValue | None = None
    ReturnConsumedCapacity: DynamoDBReturnConsumedCapacity | None = None
    ReturnItemCollectionMetrics: DynamoDBReturnItemCollectionMetrics | None = None
    UpdateExpression: StrictStr | None = None
    ConditionExpression: StrictStr | None = None
    ExpressionAttributeNames: dict[StrictStr, StrictStr] | None = None
    ExpressionAttributeValues: dict[StrictStr, DynamoDBAttributeValueInput] | None = None
    ReturnValuesOnConditionCheckFailure: DynamoDBReturnValuesOnConditionCheckFailure | None = None
