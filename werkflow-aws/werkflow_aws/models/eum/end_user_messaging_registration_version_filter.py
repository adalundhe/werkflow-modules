from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationVersionFilter(BaseModel):
    Name: Literal['registration-version-status']
    Values: list[StrictStr]
