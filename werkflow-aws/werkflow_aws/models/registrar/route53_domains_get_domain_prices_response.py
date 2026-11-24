from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_domains_domain_price import Route53DomainsDomainPrice


class Route53DomainsGetDomainPricesResponse(BaseModel):
    DomainPrice: Route53DomainsDomainPrice | None = None
    ResponseMetadata: dict[str, Any] | None = None
