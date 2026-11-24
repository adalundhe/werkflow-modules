from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ResetFpgaImageAttributeRequest(BaseModel):
    FpgaImageId: StrictStr
    DryRun: StrictBool | None = None
    Attribute: Literal['loadPermission'] | None = None
