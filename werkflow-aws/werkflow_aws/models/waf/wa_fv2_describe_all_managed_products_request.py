from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class WAFv2DescribeAllManagedProductsRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
