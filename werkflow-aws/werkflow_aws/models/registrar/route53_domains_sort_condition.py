from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class Route53DomainsSortCondition(BaseModel):
    Name: Literal['DomainName', 'Expiry']
    SortOrder: Literal['ASC', 'DESC']
