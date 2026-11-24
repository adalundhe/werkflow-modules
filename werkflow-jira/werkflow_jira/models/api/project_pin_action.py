from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ProjectPinAction(BaseModel):
    action: StrictStr | None = None
    projectIdOrKey: StrictStr | None = None
