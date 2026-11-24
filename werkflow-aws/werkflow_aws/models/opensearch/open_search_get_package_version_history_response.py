from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_package_version_history import OpenSearchPackageVersionHistory


class OpenSearchGetPackageVersionHistoryResponse(BaseModel):
    PackageID: StrictStr | None = None
    PackageVersionHistoryList: list[OpenSearchPackageVersionHistory] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
