from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_domain_status import OpenSearchDomainStatus


class OpenSearchDescribeDomainResponse(BaseModel):
    DomainStatus: OpenSearchDomainStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
