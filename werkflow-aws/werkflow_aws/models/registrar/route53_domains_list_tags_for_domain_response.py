from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_domains_tag import Route53DomainsTag


class Route53DomainsListTagsForDomainResponse(BaseModel):
    TagList: list[Route53DomainsTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
