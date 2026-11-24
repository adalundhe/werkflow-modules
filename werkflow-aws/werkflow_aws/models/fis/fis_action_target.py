from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISActionTarget(BaseModel):
    resourceType: StrictStr | None = None
