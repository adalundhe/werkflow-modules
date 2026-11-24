from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_domains_billing_record import Route53DomainsBillingRecord


class Route53DomainsViewBillingResponse(BaseModel):
    NextPageMarker: StrictStr | None = None
    BillingRecords: list[Route53DomainsBillingRecord] | None = None
    ResponseMetadata: dict[str, Any] | None = None
