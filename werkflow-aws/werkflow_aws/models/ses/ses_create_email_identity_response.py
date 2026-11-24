from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ses_dkim_attributes import SESDkimAttributes


class SESCreateEmailIdentityResponse(BaseModel):
    IdentityType: StrictStr | None = None
    VerifiedForSendingStatus: StrictBool | None = None
    DkimAttributes: SESDkimAttributes | None = None
    ResponseMetadata: dict[str, Any] | None = None
