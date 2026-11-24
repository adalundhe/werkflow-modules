from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class Route53CidrCollectionChange(BaseModel):
    LocationName: StrictStr
    Action: Literal['PUT', 'DELETE_IF_EXISTS']
    CidrList: list[StrictStr]
