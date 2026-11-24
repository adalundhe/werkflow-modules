from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_domains_price_with_currency import Route53DomainsPriceWithCurrency


class Route53DomainsDomainPrice(BaseModel):
    Name: StrictStr | None = None
    RegistrationPrice: Route53DomainsPriceWithCurrency | None = None
    TransferPrice: Route53DomainsPriceWithCurrency | None = None
    RenewalPrice: Route53DomainsPriceWithCurrency | None = None
    ChangeOwnershipPrice: Route53DomainsPriceWithCurrency | None = None
    RestorationPrice: Route53DomainsPriceWithCurrency | None = None
