from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_package_version_summary import IoTPackageVersionSummary


class IoTListPackageVersionsResponse(BaseModel):
    packageVersionSummaries: list[IoTPackageVersionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
