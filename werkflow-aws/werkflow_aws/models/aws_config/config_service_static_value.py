from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceStaticValue(BaseModel):
    Values: list[StrictStr] | None = None
