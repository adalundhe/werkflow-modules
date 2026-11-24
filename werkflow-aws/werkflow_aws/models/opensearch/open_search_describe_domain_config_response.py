from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_domain_config import OpenSearchDomainConfig


class OpenSearchDescribeDomainConfigResponse(BaseModel):
    DomainConfig: OpenSearchDomainConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
