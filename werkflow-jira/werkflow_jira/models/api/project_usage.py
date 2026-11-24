from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectUsage(BaseModel):
    id: StrictStr | None = None
