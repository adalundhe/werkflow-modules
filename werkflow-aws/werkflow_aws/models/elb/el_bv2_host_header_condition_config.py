from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2HostHeaderConditionConfig(BaseModel):
    Values: list[StrictStr] | None = None
    RegexValues: list[StrictStr] | None = None
