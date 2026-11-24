from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingNumberPreferenceItem(BaseModel):
    PreferenceType: list[Literal['StartsWith', 'EndsWith', 'Contains', 'ExactMatch']]
    Filter: list[StrictStr]
