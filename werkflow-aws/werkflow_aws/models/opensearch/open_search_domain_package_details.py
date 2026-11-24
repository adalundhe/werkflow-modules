from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .open_search_error_details import OpenSearchErrorDetails
from .open_search_package_association_configuration import OpenSearchPackageAssociationConfiguration


class OpenSearchDomainPackageDetails(BaseModel):
    PackageID: StrictStr | None = None
    PackageName: StrictStr | None = None
    PackageType: StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
    DomainName: StrictStr | None = None
    DomainPackageStatus: StrictStr | None = None
    PackageVersion: StrictStr | None = None
    PrerequisitePackageIDList: list[StrictStr] | None = None
    ReferencePath: StrictStr | None = None
    ErrorDetails: OpenSearchErrorDetails | None = None
    AssociationConfiguration: OpenSearchPackageAssociationConfiguration | None = None
