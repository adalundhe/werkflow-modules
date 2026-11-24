from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DuplicatePlanRequest(BaseModel):
    name: StrictStr | None = None
