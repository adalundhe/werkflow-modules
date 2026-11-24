from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_domains_filter_condition import Route53DomainsFilterCondition
from .route53_domains_sort_condition import Route53DomainsSortCondition


class Route53DomainsListDomainsRequest(BaseModel):
    FilterConditions: list[Route53DomainsFilterCondition] | None = None
    SortCondition: Route53DomainsSortCondition | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
