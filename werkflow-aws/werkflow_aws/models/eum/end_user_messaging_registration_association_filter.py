from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingRegistrationAssociationFilter(BaseModel):
    Name: Literal['resource-type', 'iso-country-code']
    Values: list[StrictStr]
