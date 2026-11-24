from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowDeleteFlowRequest(BaseModel):
    flowName: StrictStr
    forceDelete: StrictBool | None = None
