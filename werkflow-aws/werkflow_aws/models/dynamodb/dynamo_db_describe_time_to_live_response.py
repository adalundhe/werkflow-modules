from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_time_to_live_description import DynamoDBTimeToLiveDescription


class DynamoDBDescribeTimeToLiveResponse(BaseModel):
    TimeToLiveDescription: DynamoDBTimeToLiveDescription | None = None
