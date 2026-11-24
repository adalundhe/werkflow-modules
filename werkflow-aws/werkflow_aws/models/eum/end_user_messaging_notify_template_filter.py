from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingNotifyTemplateFilter(BaseModel):
    Name: Literal['template-type', 'channels', 'tier-access', 'supported-countries', 'language-code', 'supported-voice-ids']
    Values: list[StrictStr]
