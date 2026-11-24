from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_search_schema_element_type import DynamoDBSearchSchemaElementType


class DynamoDBSearchSchemaElement(BaseModel):
    AttributeName: StrictStr
    SearchSchemaElementType: DynamoDBSearchSchemaElementType
