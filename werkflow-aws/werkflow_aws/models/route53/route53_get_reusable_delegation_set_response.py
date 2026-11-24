from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_delegation_set_model import Route53DelegationSetModel


class Route53GetReusableDelegationSetResponse(BaseModel):
    DelegationSet: Route53DelegationSetModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
