from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComputeOptimizerJobFilter(BaseModel):
    name: Literal['ResourceType', 'JobStatus'] | None = None
    values: list[StrictStr] | None = None
