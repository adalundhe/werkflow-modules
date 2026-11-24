from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSKernelCapabilities(BaseModel):
    add: list[StrictStr] | None = None
    drop: list[StrictStr] | None = None
