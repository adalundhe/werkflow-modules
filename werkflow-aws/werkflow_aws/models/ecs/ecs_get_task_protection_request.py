from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSGetTaskProtectionRequest(BaseModel):
    cluster: StrictStr
    tasks: list[StrictStr] | None = None
