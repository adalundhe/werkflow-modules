from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_package_summary import IoTPackageSummary


class IoTListPackagesResponse(BaseModel):
    packageSummaries: list[IoTPackageSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
