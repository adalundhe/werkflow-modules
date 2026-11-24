from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LexErrorLogSettings(BaseModel):
    enabled: StrictBool | None = None
