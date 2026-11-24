from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesModificationState(BaseModel):
    Resource: StrictStr | None = None
    State: StrictStr | None = None
