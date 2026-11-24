from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class QuickSightFailedKeyRegistrationEntry(BaseModel):
    KeyArn: StrictStr | None = None
    Message: StrictStr | None = None
    StatusCode: StrictInt | None = None
    SenderFault: StrictBool | None = None
