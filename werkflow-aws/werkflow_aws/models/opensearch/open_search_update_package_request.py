from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_package_configuration import OpenSearchPackageConfiguration
from .open_search_package_encryption_options import OpenSearchPackageEncryptionOptions
from .open_search_package_source import OpenSearchPackageSource


class OpenSearchUpdatePackageRequest(BaseModel):
    PackageID: StrictStr
    PackageSource: OpenSearchPackageSource
    PackageDescription: StrictStr | None = None
    CommitMessage: StrictStr | None = None
    PackageConfiguration: OpenSearchPackageConfiguration | None = None
    PackageEncryptionOptions: OpenSearchPackageEncryptionOptions | None = None
