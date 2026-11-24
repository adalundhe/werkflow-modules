from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AthenaDeleteWorkGroupRequest(BaseModel):
    WorkGroup: StrictStr
    RecursiveDeleteOption: StrictBool | None = None
