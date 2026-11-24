from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .cognito_idp_routing_type import CognitoIDPRoutingType


class CognitoIDPCreateUserPoolDomainResponse(BaseModel):
    ManagedLoginVersion: StrictInt | None = None
    CloudFrontDomain: StrictStr | None = None
    Routing: CognitoIDPRoutingType | None = None
    ResponseMetadata: dict[str, Any] | None = None
