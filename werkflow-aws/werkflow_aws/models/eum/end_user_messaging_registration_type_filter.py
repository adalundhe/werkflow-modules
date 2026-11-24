from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationTypeFilter(BaseModel):
    Name: Literal['supported-association-resource-type', 'supported-association-iso-country-code']
    Values: list[StrictStr]
