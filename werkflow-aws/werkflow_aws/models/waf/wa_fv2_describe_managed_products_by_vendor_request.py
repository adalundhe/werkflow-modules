from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2DescribeManagedProductsByVendorRequest(BaseModel):
    VendorName: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
