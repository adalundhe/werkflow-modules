from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class PinpointSMSChannelResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    CreationDate: StrictStr | None = None
    Enabled: StrictBool | None = None
    HasCredential: StrictBool | None = None
    Id: StrictStr | None = None
    IsArchived: StrictBool | None = None
    LastModifiedBy: StrictStr | None = None
    LastModifiedDate: StrictStr | None = None
    Platform: StrictStr | None = None
    PromotionalMessagesPerSecond: StrictInt | None = None
    SenderId: StrictStr | None = None
    ShortCode: StrictStr | None = None
    TransactionalMessagesPerSecond: StrictInt | None = None
    Version: StrictInt | None = None
