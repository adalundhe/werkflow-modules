from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .dynamo_db_stream_view_type import DynamoDBStreamViewType


class DynamoDBStreamSpecification(BaseModel):
    StreamEnabled: StrictBool
    StreamViewType: DynamoDBStreamViewType | None = None
