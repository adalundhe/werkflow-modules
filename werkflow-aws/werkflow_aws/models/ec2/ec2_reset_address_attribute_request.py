from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ResetAddressAttributeRequest(BaseModel):
    AllocationId: StrictStr
    Attribute: Literal['domain-name']
    DryRun: StrictBool | None = None
