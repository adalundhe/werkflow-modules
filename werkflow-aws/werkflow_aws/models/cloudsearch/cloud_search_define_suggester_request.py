from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_search_suggester import CloudSearchSuggester


class CloudSearchDefineSuggesterRequest(BaseModel):
    DomainName: StrictStr
    Suggester: CloudSearchSuggester
