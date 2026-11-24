from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingKeywordFilter(BaseModel):
    Name: Literal['keyword-action']
    Values: list[StrictStr]
