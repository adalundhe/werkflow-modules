from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSGetKeyPolicyRequest(BaseModel):
    KeyId: StrictStr
    PolicyName: StrictStr | None = None
