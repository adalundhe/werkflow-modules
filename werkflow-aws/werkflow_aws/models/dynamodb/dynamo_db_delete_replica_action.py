from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDeleteReplicaAction(BaseModel):
    RegionName: StrictStr
