from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_domains_domain_price import Route53DomainsDomainPrice


class Route53DomainsListPricesResponse(BaseModel):
    Prices: list[Route53DomainsDomainPrice] | None = None
    NextPageMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
