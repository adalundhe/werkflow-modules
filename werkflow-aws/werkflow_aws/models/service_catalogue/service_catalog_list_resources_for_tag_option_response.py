from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_resource_detail import ServiceCatalogResourceDetail


class ServiceCatalogListResourcesForTagOptionResponse(BaseModel):
    ResourceDetails: list[ServiceCatalogResourceDetail] | None = None
    PageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
