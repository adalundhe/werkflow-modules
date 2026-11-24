from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectArchetype(BaseModel):
    realType: StrictStr | None = None
    style: StrictStr | None = None
    type: StrictStr | None = None
