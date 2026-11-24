from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointNumberValidateRequest(BaseModel):
    IsoCountryCode: StrictStr | None = None
    PhoneNumber: StrictStr | None = None
