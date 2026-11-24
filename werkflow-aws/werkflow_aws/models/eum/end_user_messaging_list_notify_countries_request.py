from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EndUserMessagingListNotifyCountriesRequest(BaseModel):
    Channels: list[Literal['SMS', 'VOICE', 'MMS', 'RCS']] | None = None
    UseCases: list[Literal['CODE_VERIFICATION']] | None = None
    Tier: Literal['BASIC', 'ADVANCED'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
