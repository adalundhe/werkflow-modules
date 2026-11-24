from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_domain_info import OpenSearchDomainInfo


class OpenSearchListDomainNamesResponse(BaseModel):
    DomainNames: list[OpenSearchDomainInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
