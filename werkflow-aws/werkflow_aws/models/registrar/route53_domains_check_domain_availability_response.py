from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_domains_price_with_currency import Route53DomainsPriceWithCurrency


class Route53DomainsCheckDomainAvailabilityResponse(BaseModel):
    Availability: StrictStr | None = None
    Price: Route53DomainsPriceWithCurrency | None = None
    ResponseMetadata: dict[str, Any] | None = None
