from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectRouteFilters(BaseModel):
    routeDirection: Literal['accepted', 'advertised'] | None = None
    addressFamily: Literal['ipv4', 'ipv6'] | None = None
    cidrs: list[StrictStr] | None = None
    asPath: list[StrictInt] | None = None
    communities: list[StrictStr] | None = None
