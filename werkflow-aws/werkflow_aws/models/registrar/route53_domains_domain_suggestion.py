from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_domains_price_with_currency import Route53DomainsPriceWithCurrency


class Route53DomainsDomainSuggestion(BaseModel):
    DomainName: StrictStr | None = None
    Availability: StrictStr | None = None
    Price: Route53DomainsPriceWithCurrency | None = None
