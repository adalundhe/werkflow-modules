from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput
from .dynamo_db_comparison_operator import DynamoDBComparisonOperator


class DynamoDBExpectedAttributeValue(BaseModel):
    Value: DynamoDBAttributeValueInput | None = None
    Exists: StrictBool | None = None
    ComparisonOperator: DynamoDBComparisonOperator | None = None
    AttributeValueList: list[DynamoDBAttributeValueInput] | None = None
