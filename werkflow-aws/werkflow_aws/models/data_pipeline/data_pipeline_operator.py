from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataPipelineOperator(BaseModel):
    type: Literal['EQ', 'REF_EQ', 'LE', 'GE', 'BETWEEN'] | None = None
    values: list[StrictStr] | None = None
