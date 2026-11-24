from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .open_search_error_details import OpenSearchErrorDetails
from .open_search_package_configuration import OpenSearchPackageConfiguration
from .open_search_package_encryption_options import OpenSearchPackageEncryptionOptions
from .open_search_package_vending_options import OpenSearchPackageVendingOptions
from .open_search_plugin_properties import OpenSearchPluginProperties


class OpenSearchPackageDetails(BaseModel):
    PackageID: StrictStr | None = None
    PackageName: StrictStr | None = None
    PackageType: StrictStr | None = None
    PackageDescription: StrictStr | None = None
    PackageStatus: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    LastUpdatedAt: datetime.datetime | StrictStr | None = None
    AvailablePackageVersion: StrictStr | None = None
    ErrorDetails: OpenSearchErrorDetails | None = None
    EngineVersion: StrictStr | None = None
    AvailablePluginProperties: OpenSearchPluginProperties | None = None
    AvailablePackageConfiguration: OpenSearchPackageConfiguration | None = None
    AllowListedUserList: list[StrictStr] | None = None
    PackageOwner: StrictStr | None = None
    PackageVendingOptions: OpenSearchPackageVendingOptions | None = None
    PackageEncryptionOptions: OpenSearchPackageEncryptionOptions | None = None
