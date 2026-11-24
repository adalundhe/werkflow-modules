from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_domains_domain_suggestion import Route53DomainsDomainSuggestion


class Route53DomainsGetDomainSuggestionsResponse(BaseModel):
    SuggestionsList: list[Route53DomainsDomainSuggestion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
