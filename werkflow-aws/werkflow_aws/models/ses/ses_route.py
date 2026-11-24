from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESRoute(BaseModel):
    Region: StrictStr | None = None
