from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayInstanceIdDetail(BaseModel):
    Id: StrictStr | None = None
