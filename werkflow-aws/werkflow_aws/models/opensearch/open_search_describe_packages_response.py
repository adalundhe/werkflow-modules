from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_package_details import OpenSearchPackageDetails


class OpenSearchDescribePackagesResponse(BaseModel):
    PackageDetailsList: list[OpenSearchPackageDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
