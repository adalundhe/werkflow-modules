from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class FMSPolicyTypeScope(BaseModel):
    PolicyTypes: list[StrictStr] | None = None
    AllPolicyTypesEnabled: StrictBool | None = None
