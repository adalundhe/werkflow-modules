from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt


class CostExplorerTotalImpactFilter(BaseModel):
    NumericOperator: Literal['EQUAL', 'GREATER_THAN_OR_EQUAL', 'LESS_THAN_OR_EQUAL', 'GREATER_THAN', 'LESS_THAN', 'BETWEEN']
    StartValue: StrictFloat | StrictInt
    EndValue: StrictFloat | StrictInt | None = None
