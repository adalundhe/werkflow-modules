from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2SingleHeader(BaseModel):
    Name: StrictStr | None = None
