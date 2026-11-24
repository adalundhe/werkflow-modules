from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingCountryLaunchStatusFilter(BaseModel):
    Name: Literal['country-launch-status']
    Values: list[StrictStr]
