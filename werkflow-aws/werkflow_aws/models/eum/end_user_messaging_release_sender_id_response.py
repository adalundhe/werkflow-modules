from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingReleaseSenderIdResponse(BaseModel):
    SenderIdArn: StrictStr | None = None
    SenderId: StrictStr | None = None
    IsoCountryCode: StrictStr | None = None
    MessageTypes: list[StrictStr] | None = None
    MonthlyLeasingPrice: StrictStr | None = None
    Registered: StrictBool | None = None
    RegistrationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
