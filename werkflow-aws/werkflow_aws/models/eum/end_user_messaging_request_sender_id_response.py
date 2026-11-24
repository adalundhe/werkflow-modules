from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .end_user_messaging_tag import EndUserMessagingTag


class EndUserMessagingRequestSenderIdResponse(BaseModel):
    SenderIdArn: StrictStr | None = None
    SenderId: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    MessageTypes: list[StrictStr] | None = None
    MonthlyLeasingPrice: StrictStr | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    Registered: StrictBool | None = None
    Tags: list[EndUserMessagingTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
