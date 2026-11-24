from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .swf_domain_configuration import SWFDomainConfiguration
from .swf_domain_info import SWFDomainInfo


class SWFDescribeDomainResponse(BaseModel):
    domainInfo: SWFDomainInfo | None = None
    configuration: SWFDomainConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
