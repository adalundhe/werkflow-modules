from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_package_association_configuration import OpenSearchPackageAssociationConfiguration


class OpenSearchPackageDetailsForAssociation(BaseModel):
    PackageID: StrictStr
    PrerequisitePackageIDList: list[StrictStr] | None = None
    AssociationConfiguration: OpenSearchPackageAssociationConfiguration | None = None
