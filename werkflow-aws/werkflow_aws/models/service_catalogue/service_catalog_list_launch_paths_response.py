from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_launch_path_summary import ServiceCatalogLaunchPathSummary


class ServiceCatalogListLaunchPathsResponse(BaseModel):
    LaunchPathSummaries: list[ServiceCatalogLaunchPathSummary] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
