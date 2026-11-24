from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_discovered_resource import FMSDiscoveredResource


class FMSListDiscoveredResourcesResponse(BaseModel):
    Items: list[FMSDiscoveredResource] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
