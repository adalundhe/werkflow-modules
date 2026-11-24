from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexCustomPayload(BaseModel):
    value: StrictStr | None = None
