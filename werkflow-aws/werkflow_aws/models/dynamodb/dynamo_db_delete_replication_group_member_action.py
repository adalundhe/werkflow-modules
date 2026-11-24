from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDeleteReplicationGroupMemberAction(BaseModel):
    RegionName: StrictStr
