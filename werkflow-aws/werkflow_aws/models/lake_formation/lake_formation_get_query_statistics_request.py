from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationGetQueryStatisticsRequest(BaseModel):
    QueryId: StrictStr
