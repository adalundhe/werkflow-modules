from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ACMDnsNameFilter(BaseModel):
    Value: StrictStr
    ComparisonOperator: Literal['CONTAINS', 'EQUALS']
