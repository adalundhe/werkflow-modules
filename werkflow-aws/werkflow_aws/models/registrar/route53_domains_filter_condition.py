from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53DomainsFilterCondition(BaseModel):
    Name: Literal['DomainName', 'Expiry']
    Operator: Literal['LE', 'GE', 'BEGINS_WITH']
    Values: list[StrictStr]
