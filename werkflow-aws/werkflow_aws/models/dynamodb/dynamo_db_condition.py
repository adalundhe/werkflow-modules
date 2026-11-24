from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_attribute_value_input import DynamoDBAttributeValueInput
from .dynamo_db_comparison_operator import DynamoDBComparisonOperator


class DynamoDBCondition(BaseModel):
    ComparisonOperator: DynamoDBComparisonOperator
    AttributeValueList: list[DynamoDBAttributeValueInput] | None = None
