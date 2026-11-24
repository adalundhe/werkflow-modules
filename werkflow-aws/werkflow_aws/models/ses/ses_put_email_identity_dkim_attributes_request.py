from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SESPutEmailIdentityDkimAttributesRequest(BaseModel):
    EmailIdentity: StrictStr
    SigningEnabled: StrictBool | None = None
