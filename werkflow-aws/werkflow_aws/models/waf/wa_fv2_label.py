from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2Label(BaseModel):
    Name: StrictStr | None = None
