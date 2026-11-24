from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_domain_package_details import OpenSearchDomainPackageDetails


class OpenSearchDissociatePackagesResponse(BaseModel):
    DomainPackageDetailsList: list[OpenSearchDomainPackageDetails] | None = None
    ResponseMetadata: dict[str, Any] | None = None
