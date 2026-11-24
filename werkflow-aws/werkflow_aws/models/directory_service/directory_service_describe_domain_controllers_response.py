from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_domain_controller import DirectoryServiceDomainController


class DirectoryServiceDescribeDomainControllersResponse(BaseModel):
    DomainControllers: list[DirectoryServiceDomainController] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
