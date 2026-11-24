from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBDeleteGlobalTableWitnessGroupMemberAction(BaseModel):
    RegionName: StrictStr
