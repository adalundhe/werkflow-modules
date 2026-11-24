from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_product_v2 import SecurityHubProductV2


class SecurityHubDescribeProductsV2Response(BaseModel):
    ProductsV2: list[SecurityHubProductV2] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
