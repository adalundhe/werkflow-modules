from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_tag import DynamoDBTag


class DynamoDBListTagsOfResourceResponse(BaseModel):
    Tags: list[DynamoDBTag] | None = None
    NextToken: StrictStr | None = None
