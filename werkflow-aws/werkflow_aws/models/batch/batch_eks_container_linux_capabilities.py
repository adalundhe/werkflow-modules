from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEksContainerLinuxCapabilities(BaseModel):
    add: list[StrictStr] | None = None
    drop: list[StrictStr] | None = None
