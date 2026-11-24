from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesUserStorage(BaseModel):
    Capacity: StrictStr | None = None
