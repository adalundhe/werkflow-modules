from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SESPutEmailIdentityFeedbackAttributesRequest(BaseModel):
    EmailIdentity: StrictStr
    EmailForwardingEnabled: StrictBool | None = None
