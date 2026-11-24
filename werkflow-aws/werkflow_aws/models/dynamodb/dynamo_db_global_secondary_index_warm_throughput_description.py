from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .dynamo_db_index_status import DynamoDBIndexStatus


class DynamoDBGlobalSecondaryIndexWarmThroughputDescription(BaseModel):
    ReadUnitsPerSecond: StrictInt | None = None
    WriteUnitsPerSecond: StrictInt | None = None
    Status: DynamoDBIndexStatus | None = None
