from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRaySegment(BaseModel):
    Id: StrictStr | None = None
    Document: StrictStr | None = None
