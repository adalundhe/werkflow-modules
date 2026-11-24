from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataSyncTaskFilter(BaseModel):
    Name: Literal['LocationId', 'CreationTime']
    Values: list[StrictStr]
    Operator: Literal['Equals', 'NotEquals', 'In', 'LessThanOrEqual', 'LessThan', 'GreaterThanOrEqual', 'GreaterThan', 'Contains', 'NotContains', 'BeginsWith']
