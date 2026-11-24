from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ResetImageAttributeRequest(BaseModel):
    Attribute: Literal['launchPermission']
    ImageId: StrictStr
    DryRun: StrictBool | None = None
