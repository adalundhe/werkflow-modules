from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .route53_account_limit import Route53AccountLimit


class Route53GetAccountLimitResponse(BaseModel):
    Limit: Route53AccountLimit | None = None
    Count: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
