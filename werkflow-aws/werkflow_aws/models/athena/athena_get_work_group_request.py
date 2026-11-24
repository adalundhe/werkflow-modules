from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaGetWorkGroupRequest(BaseModel):
    WorkGroup: StrictStr
