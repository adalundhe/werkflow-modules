from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_package_details_for_association import OpenSearchPackageDetailsForAssociation


class OpenSearchAssociatePackagesRequest(BaseModel):
    PackageList: list[OpenSearchPackageDetailsForAssociation]
    DomainName: StrictStr
