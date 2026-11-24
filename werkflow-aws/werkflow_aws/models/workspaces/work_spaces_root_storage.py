from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesRootStorage(BaseModel):
    Capacity: StrictStr | None = None
