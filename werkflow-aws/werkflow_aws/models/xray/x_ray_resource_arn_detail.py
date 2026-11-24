from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayResourceARNDetail(BaseModel):
    ARN: StrictStr | None = None
