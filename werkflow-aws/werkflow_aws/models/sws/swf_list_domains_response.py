from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .swf_domain_info import SWFDomainInfo


class SWFListDomainsResponse(BaseModel):
    domainInfos: list[SWFDomainInfo] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
