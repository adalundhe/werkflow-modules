from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class RDSBacktrackDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    BacktrackTo: datetime.datetime | StrictStr
    Force: StrictBool | None = None
    UseEarliestTimeOnPointInTimeUnavailable: StrictBool | None = None
