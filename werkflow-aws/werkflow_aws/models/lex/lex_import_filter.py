from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexImportFilter(BaseModel):
    name: Literal['ImportResourceType']
    values: list[StrictStr]
    operator: Literal['CO', 'EQ']
