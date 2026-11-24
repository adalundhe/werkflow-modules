from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_product import SecurityHubProduct


class SecurityHubDescribeProductsResponse(BaseModel):
    Products: list[SecurityHubProduct] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
