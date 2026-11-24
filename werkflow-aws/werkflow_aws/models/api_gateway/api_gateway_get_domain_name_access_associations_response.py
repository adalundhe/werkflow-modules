from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_domain_name_access_association import APIGatewayDomainNameAccessAssociation


class APIGatewayGetDomainNameAccessAssociationsResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayDomainNameAccessAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
