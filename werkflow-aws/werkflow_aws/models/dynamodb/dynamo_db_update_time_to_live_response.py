from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_time_to_live_specification import DynamoDBTimeToLiveSpecification


class DynamoDBUpdateTimeToLiveResponse(BaseModel):
    TimeToLiveSpecification: DynamoDBTimeToLiveSpecification | None = None
