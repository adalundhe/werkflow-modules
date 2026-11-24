from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_tag_option_detail import ServiceCatalogTagOptionDetail


class ServiceCatalogCreateTagOptionResponse(BaseModel):
    TagOptionDetail: ServiceCatalogTagOptionDetail | None = None
    ResponseMetadata: dict[str, Any] | None = None
