from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DescribeFpgaImageAttributeRequest(BaseModel):
    FpgaImageId: StrictStr
    Attribute: Literal['description', 'name', 'loadPermission', 'productCodes']
    DryRun: StrictBool | None = None
