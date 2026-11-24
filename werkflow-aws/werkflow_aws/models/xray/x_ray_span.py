from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRaySpan(BaseModel):
    Id: StrictStr | None = None
    Document: StrictStr | None = None
