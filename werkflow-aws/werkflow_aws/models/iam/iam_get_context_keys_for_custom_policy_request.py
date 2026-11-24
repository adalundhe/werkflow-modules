from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetContextKeysForCustomPolicyRequest(BaseModel):
    PolicyInputList: list[StrictStr]
