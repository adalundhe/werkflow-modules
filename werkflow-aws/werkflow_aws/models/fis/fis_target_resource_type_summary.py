from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISTargetResourceTypeSummary(BaseModel):
    resourceType: StrictStr | None = None
    description: StrictStr | None = None
