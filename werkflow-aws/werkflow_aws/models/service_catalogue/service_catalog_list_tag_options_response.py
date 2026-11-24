from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_tag_option_detail import ServiceCatalogTagOptionDetail


class ServiceCatalogListTagOptionsResponse(BaseModel):
    TagOptionDetails: list[ServiceCatalogTagOptionDetail] | None = None
    PageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
