from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetContextKeysForPrincipalPolicyRequest(BaseModel):
    PolicySourceArn: StrictStr
    PolicyInputList: list[StrictStr] | None = None
