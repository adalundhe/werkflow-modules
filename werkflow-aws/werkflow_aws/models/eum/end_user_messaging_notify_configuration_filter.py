from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingNotifyConfigurationFilter(BaseModel):
    Name: Literal['display-name', 'enabled-countries', 'enabled-channels', 'default-template', 'default-pool', 'use-case', 'status', 'deletion-protection-enabled', 'tier-upgrade-status']
    Values: list[StrictStr]
