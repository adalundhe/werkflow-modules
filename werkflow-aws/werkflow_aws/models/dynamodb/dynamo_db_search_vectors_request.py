from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_attribute_value_model import DynamoDBAttributeValueModel


class DynamoDBSearchVectorsRequest(BaseModel):
    TableName: StrictStr
    IndexName: StrictStr
    SearchVector: list[DynamoDBAttributeValueModel]
    TopK: StrictInt
    ReturnConsumedCapacity: Literal['INDEXES', 'TOTAL', 'NONE'] | None = None
    ExpressionAttributeNames: dict[StrictStr, StrictStr] | None = None
    ExpressionAttributeValues: dict[StrictStr, DynamoDBAttributeValueModel] | None = None
    ProjectionExpression: StrictStr | None = None
    SearchConditionExpression: StrictStr | None = None
