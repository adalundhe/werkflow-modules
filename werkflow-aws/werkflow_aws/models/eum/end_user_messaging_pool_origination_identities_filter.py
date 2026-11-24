from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingPoolOriginationIdentitiesFilter(BaseModel):
    Name: Literal['iso-country-code', 'number-capability']
    Values: list[StrictStr]
