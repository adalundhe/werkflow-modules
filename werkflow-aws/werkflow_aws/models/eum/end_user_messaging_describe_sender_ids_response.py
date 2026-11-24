from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .end_user_messaging_sender_id_information import EndUserMessagingSenderIdInformation


class EndUserMessagingDescribeSenderIdsResponse(BaseModel):
    SenderIds: list[EndUserMessagingSenderIdInformation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
