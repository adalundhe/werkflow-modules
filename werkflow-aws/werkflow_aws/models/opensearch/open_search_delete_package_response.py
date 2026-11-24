from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_package_details import OpenSearchPackageDetails


class OpenSearchDeletePackageResponse(BaseModel):
    PackageDetails: OpenSearchPackageDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
