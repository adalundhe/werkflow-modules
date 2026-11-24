from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConfigServiceConnectorFilter(BaseModel):
    filterName: Literal['provider'] | None = None
    filterValues: list[StrictStr] | None = None
