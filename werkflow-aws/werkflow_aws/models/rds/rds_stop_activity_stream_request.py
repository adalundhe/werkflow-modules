from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSStopActivityStreamRequest(BaseModel):
    ResourceArn: StrictStr
    ApplyImmediately: StrictBool | None = None
