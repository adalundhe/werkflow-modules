from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ConfigServiceDescribeConformancePacksFilters(BaseModel):
    Types: list[Literal['CUSTOM', 'MANAGED']] | None = None
