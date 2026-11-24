from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingSenderIdFilter(BaseModel):
    Name: Literal['sender-id', 'iso-country-code', 'message-type', 'deletion-protection-enabled', 'registered']
    Values: list[StrictStr]
