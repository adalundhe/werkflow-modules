from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RedshiftNodeConfigurationOptionsFilter(BaseModel):
    Name: Literal['NodeType', 'NumberOfNodes', 'EstimatedDiskUtilizationPercent', 'Mode'] | None = None
    Operator: Literal['eq', 'lt', 'gt', 'le', 'ge', 'in', 'between'] | None = None
    Values: list[StrictStr] | None = None
