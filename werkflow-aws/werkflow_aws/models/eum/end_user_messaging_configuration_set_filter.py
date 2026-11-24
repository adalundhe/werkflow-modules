from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingConfigurationSetFilter(BaseModel):
    Name: Literal['event-destination-name', 'matching-event-types', 'default-message-type', 'default-sender-id', 'default-message-feedback-enabled', 'protect-configuration-id']
    Values: list[StrictStr]
