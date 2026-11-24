from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingProtectConfigurationFilter(BaseModel):
    Name: Literal['account-default', 'deletion-protection-enabled']
    Values: list[StrictStr]
