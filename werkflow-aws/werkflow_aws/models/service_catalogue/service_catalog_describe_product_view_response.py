from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_product_view_summary import ServiceCatalogProductViewSummary
from .service_catalog_provisioning_artifact import ServiceCatalogProvisioningArtifact


class ServiceCatalogDescribeProductViewResponse(BaseModel):
    ProductViewSummary: ServiceCatalogProductViewSummary | None = None
    ProvisioningArtifacts: list[ServiceCatalogProvisioningArtifact] | None = None
    ResponseMetadata: dict[str, Any] | None = None
