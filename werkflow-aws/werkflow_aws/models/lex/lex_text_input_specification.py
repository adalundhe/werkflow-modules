from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LexTextInputSpecification(BaseModel):
    startTimeoutMs: StrictInt | None = None
