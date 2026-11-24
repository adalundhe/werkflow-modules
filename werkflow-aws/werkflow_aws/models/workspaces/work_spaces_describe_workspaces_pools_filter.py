from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WorkSpacesDescribeWorkspacesPoolsFilter(BaseModel):
    Name: Literal['PoolName']
    Values: list[StrictStr]
    Operator: Literal['EQUALS', 'NOTEQUALS', 'CONTAINS', 'NOTCONTAINS']
