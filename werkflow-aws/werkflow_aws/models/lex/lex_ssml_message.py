from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexSSMLMessage(BaseModel):
    value: StrictStr | None = None
