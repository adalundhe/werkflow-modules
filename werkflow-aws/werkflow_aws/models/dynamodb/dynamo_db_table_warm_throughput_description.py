from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .dynamo_db_table_status import DynamoDBTableStatus


class DynamoDBTableWarmThroughputDescription(BaseModel):
    ReadUnitsPerSecond: StrictInt | None = None
    WriteUnitsPerSecond: StrictInt | None = None
    Status: DynamoDBTableStatus | None = None
