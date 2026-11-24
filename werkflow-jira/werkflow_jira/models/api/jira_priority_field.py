from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraPriorityField(BaseModel):
    priorityId: StrictStr | None = None
