from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StatusProjectUsage(BaseModel):
    id: StrictStr | None = None
