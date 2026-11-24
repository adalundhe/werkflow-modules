from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsDeleteTagsForDomainRequest(BaseModel):
    DomainName: StrictStr
    TagsToDelete: list[StrictStr]
