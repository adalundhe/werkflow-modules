from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComputeOptimizerEnrollmentFilter(BaseModel):
    name: Literal['Status'] | None = None
    values: list[StrictStr] | None = None
