from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class ComputeOptimizerOrderBy(BaseModel):
    dimension: Literal['SavingsValue', 'SavingsValueAfterDiscount'] | None = None
    order: Literal['Asc', 'Desc'] | None = None
