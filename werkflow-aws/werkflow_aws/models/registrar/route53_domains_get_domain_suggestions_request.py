from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class Route53DomainsGetDomainSuggestionsRequest(BaseModel):
    DomainName: StrictStr
    SuggestionCount: StrictInt
    OnlyAvailable: StrictBool
    OnlyStandardPrices: StrictBool | None = None
