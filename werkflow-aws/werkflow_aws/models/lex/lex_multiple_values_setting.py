from __future__ import annotations
from pydantic import BaseModel, StrictBool


class LexMultipleValuesSetting(BaseModel):
    allowMultipleValues: StrictBool | None = None
