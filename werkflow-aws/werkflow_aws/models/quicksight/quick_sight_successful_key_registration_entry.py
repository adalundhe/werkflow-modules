from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightSuccessfulKeyRegistrationEntry(BaseModel):
    KeyArn: StrictStr | None = None
    StatusCode: StrictInt | None = None
