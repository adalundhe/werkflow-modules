from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .open_search_package_configuration import OpenSearchPackageConfiguration
from .open_search_package_encryption_options import OpenSearchPackageEncryptionOptions
from .open_search_package_source import OpenSearchPackageSource
from .open_search_package_vending_options import OpenSearchPackageVendingOptions


class OpenSearchCreatePackageRequest(BaseModel):
    PackageName: StrictStr
    PackageType: Literal['TXT-DICTIONARY', 'ZIP-PLUGIN', 'PACKAGE-LICENSE', 'PACKAGE-CONFIG']
    PackageSource: OpenSearchPackageSource
    PackageDescription: StrictStr | None = None
    PackageConfiguration: OpenSearchPackageConfiguration | None = None
    EngineVersion: StrictStr | None = None
    PackageVendingOptions: OpenSearchPackageVendingOptions | None = None
    PackageEncryptionOptions: OpenSearchPackageEncryptionOptions | None = None
