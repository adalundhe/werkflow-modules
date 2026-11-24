from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SESIdentityInfo(BaseModel):
    IdentityType: StrictStr | None = None
    IdentityName: StrictStr | None = None
    SendingEnabled: StrictBool | None = None
    VerificationStatus: StrictStr | None = None
