from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_product_view_detail import ServiceCatalogProductViewDetail
from .service_catalog_provisioning_artifact_detail import ServiceCatalogProvisioningArtifactDetail
from .service_catalog_tag import ServiceCatalogTag


class ServiceCatalogCreateProductResponse(BaseModel):
    ProductViewDetail: ServiceCatalogProductViewDetail | None = None
    ProvisioningArtifactDetail: ServiceCatalogProvisioningArtifactDetail | None = None
    Tags: list[ServiceCatalogTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
