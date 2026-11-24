from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingProtectConfigurationRuleSetNumberOverrideFilterItem(BaseModel):
    Name: Literal['iso-country-code', 'destination-phone-number-begins-with', 'action', 'expires-before', 'expires-after', 'created-before', 'created-after']
    Values: list[StrictStr]
