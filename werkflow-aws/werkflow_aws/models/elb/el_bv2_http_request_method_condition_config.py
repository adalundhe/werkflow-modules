from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2HttpRequestMethodConditionConfig(BaseModel):
    Values: list[StrictStr] | None = None
