from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingOptedOutFilter(BaseModel):
    Name: Literal['end-user-opted-out']
    Values: list[StrictStr]
