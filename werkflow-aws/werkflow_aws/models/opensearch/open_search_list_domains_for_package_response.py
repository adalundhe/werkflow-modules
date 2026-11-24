from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_domain_package_details import OpenSearchDomainPackageDetails


class OpenSearchListDomainsForPackageResponse(BaseModel):
    DomainPackageDetailsList: list[OpenSearchDomainPackageDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
