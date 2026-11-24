from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESGetEmailIdentityRequest(BaseModel):
    EmailIdentity: StrictStr
