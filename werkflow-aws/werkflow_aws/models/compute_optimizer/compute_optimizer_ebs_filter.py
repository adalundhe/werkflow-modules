from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComputeOptimizerEBSFilter(BaseModel):
    name: Literal['Finding'] | None = None
    values: list[StrictStr] | None = None
