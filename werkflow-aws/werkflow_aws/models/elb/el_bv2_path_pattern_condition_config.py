from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2PathPatternConditionConfig(BaseModel):
    Values: list[StrictStr] | None = None
    RegexValues: list[StrictStr] | None = None
