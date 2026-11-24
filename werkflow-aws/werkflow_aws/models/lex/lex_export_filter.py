from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LexExportFilter(BaseModel):
    name: Literal['ExportResourceType']
    values: list[StrictStr]
    operator: Literal['CO', 'EQ']
