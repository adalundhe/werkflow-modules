from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchInstanceRequirementsRequest(BaseModel):
    allowedInstanceTypes: list[StrictStr] | None = None
