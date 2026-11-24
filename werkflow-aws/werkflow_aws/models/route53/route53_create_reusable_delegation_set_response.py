from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_delegation_set_model import Route53DelegationSetModel


class Route53CreateReusableDelegationSetResponse(BaseModel):
    DelegationSet: Route53DelegationSetModel | None = None
    Location: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
