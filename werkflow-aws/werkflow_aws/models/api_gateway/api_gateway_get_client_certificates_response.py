from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_client_certificate import APIGatewayClientCertificate


class APIGatewayGetClientCertificatesResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayClientCertificate] | None = None
    ResponseMetadata: dict[str, Any] | None = None
