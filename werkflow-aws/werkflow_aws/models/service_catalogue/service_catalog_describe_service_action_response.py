from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_service_action_detail import ServiceCatalogServiceActionDetail


class ServiceCatalogDescribeServiceActionResponse(BaseModel):
    ServiceActionDetail: ServiceCatalogServiceActionDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
