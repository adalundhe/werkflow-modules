from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEksContainerResourceRequirements(BaseModel):
    limits: dict[StrictStr, StrictStr] | None = None
    requests: dict[StrictStr, StrictStr] | None = None
