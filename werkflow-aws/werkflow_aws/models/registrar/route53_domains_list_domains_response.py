from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_domains_domain_summary import Route53DomainsDomainSummary


class Route53DomainsListDomainsResponse(BaseModel):
    Domains: list[Route53DomainsDomainSummary] | None = None
    NextPageMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
