from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_tag import DynamoDBTag


class DynamoDBTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[DynamoDBTag]
