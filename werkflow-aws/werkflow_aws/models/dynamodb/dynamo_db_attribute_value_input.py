from __future__ import annotations
from pydantic import StrictStr
from typing import Any
from .dynamo_db_attribute_value import DynamoDBAttributeValue


DynamoDBAttributeValueInput = DynamoDBAttributeValue | dict[StrictStr, Any]
