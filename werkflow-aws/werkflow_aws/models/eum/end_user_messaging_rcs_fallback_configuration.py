from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingRcsFallbackConfiguration(BaseModel):
    Channel: Literal['SMS', 'MMS']
    MessageBody: StrictStr | None = None
    MediaUrls: list[StrictStr] | None = None
    OriginationIdentity: StrictStr | None = None
