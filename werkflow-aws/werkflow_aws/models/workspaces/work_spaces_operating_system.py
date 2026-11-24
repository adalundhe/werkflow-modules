from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesOperatingSystem(BaseModel):
    Type: StrictStr | None = None
