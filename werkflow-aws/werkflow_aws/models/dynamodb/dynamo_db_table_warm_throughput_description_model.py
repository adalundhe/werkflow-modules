from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DynamoDBTableWarmThroughputDescriptionModel(BaseModel):
    ReadUnitsPerSecond: StrictInt | None = None
    WriteUnitsPerSecond: StrictInt | None = None
    Status: StrictStr | None = None
