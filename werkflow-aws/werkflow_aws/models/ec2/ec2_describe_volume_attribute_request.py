from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DescribeVolumeAttributeRequest(BaseModel):
    Attribute: Literal['autoEnableIO', 'productCodes']
    VolumeId: StrictStr
    DryRun: StrictBool | None = None
