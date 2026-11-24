from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_time_to_live_specification import DynamoDBTimeToLiveSpecification


class DynamoDBUpdateTimeToLiveRequest(BaseModel):
    TableName: StrictStr
    TimeToLiveSpecification: DynamoDBTimeToLiveSpecification
