from __future__ import annotations
from pydantic import BaseModel
from .service_catalog_product_view_summary import ServiceCatalogProductViewSummary
from .service_catalog_provisioning_artifact import ServiceCatalogProvisioningArtifact


class ServiceCatalogProvisioningArtifactView(BaseModel):
    ProductViewSummary: ServiceCatalogProductViewSummary | None = None
    ProvisioningArtifact: ServiceCatalogProvisioningArtifact | None = None
