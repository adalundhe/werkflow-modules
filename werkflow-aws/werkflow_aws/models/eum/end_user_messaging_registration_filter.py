from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationFilter(BaseModel):
    Name: Literal['registration-type', 'registration-status']
    Values: list[StrictStr]
