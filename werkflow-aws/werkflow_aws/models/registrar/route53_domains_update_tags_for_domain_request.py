from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_domains_tag import Route53DomainsTag


class Route53DomainsUpdateTagsForDomainRequest(BaseModel):
    DomainName: StrictStr
    TagsToUpdate: list[Route53DomainsTag] | None = None
