from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointMessageResult(BaseModel):
    DeliveryStatus: StrictStr | None = None
    MessageId: StrictStr | None = None
    StatusCode: StrictInt | None = None
    StatusMessage: StrictStr | None = None
    UpdatedToken: StrictStr | None = None
