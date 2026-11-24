from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_delegation_set_model import Route53DelegationSetModel


class Route53ListReusableDelegationSetsResponse(BaseModel):
    DelegationSets: list[Route53DelegationSetModel] | None = None
    Marker: StrictStr | None = None
    IsTruncated: StrictBool | None = None
    NextMarker: StrictStr | None = None
    MaxItems: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
