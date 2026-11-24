from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .end_user_messaging_sender_id_and_country import EndUserMessagingSenderIdAndCountry
from .end_user_messaging_sender_id_filter import EndUserMessagingSenderIdFilter


class EndUserMessagingDescribeSenderIdsRequest(BaseModel):
    SenderIds: list[EndUserMessagingSenderIdAndCountry] | None = None
    Filters: list[EndUserMessagingSenderIdFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Owner: Literal['SELF', 'SHARED'] | None = None
