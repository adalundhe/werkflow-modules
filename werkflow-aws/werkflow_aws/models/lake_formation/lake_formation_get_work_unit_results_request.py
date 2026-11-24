from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LakeFormationGetWorkUnitResultsRequest(BaseModel):
    QueryId: StrictStr
    WorkUnitId: StrictInt
    WorkUnitToken: StrictStr
