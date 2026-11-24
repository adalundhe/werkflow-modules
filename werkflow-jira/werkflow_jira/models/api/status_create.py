from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StatusCreate(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    statusCategory: StrictStr | None = None
