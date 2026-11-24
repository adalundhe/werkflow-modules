from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_region_description import DirectoryServiceRegionDescription


class DirectoryServiceDescribeRegionsResponse(BaseModel):
    RegionsDescription: list[DirectoryServiceRegionDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
