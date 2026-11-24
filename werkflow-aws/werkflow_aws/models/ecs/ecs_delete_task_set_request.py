from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECSDeleteTaskSetRequest(BaseModel):
    cluster: StrictStr
    service: StrictStr
    taskSet: StrictStr
    force: StrictBool | None = None
