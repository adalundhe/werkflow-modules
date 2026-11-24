from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesComputeType(BaseModel):
    Name: StrictStr | None = None
