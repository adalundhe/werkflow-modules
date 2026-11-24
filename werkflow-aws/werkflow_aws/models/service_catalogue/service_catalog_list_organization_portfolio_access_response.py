from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_organization_node import ServiceCatalogOrganizationNode


class ServiceCatalogListOrganizationPortfolioAccessResponse(BaseModel):
    OrganizationNodes: list[ServiceCatalogOrganizationNode] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
