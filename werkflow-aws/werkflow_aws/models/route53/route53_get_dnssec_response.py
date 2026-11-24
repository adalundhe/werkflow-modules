from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_dnssec_status import Route53DNSSECStatus
from .route53_key_signing_key import Route53KeySigningKey


class Route53GetDNSSECResponse(BaseModel):
    Status: Route53DNSSECStatus | None = None
    KeySigningKeys: list[Route53KeySigningKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
