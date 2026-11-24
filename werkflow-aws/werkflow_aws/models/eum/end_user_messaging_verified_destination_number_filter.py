from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingVerifiedDestinationNumberFilter(BaseModel):
    Name: Literal['status', 'rcs-agent-id']
    Values: list[StrictStr]
