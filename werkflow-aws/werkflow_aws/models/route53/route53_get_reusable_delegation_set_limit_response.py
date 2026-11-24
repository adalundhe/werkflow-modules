from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt
from .route53_reusable_delegation_set_limit import Route53ReusableDelegationSetLimit


class Route53GetReusableDelegationSetLimitResponse(BaseModel):
    Limit: Route53ReusableDelegationSetLimit | None = None
    Count: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
