from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SetDefaultPriorityRequest(BaseModel):
    id: StrictStr | None = None
