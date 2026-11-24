from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectId(BaseModel):
    id: StrictStr | None = None
