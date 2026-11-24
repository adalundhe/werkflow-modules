from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_provisioning_artifact_detail import ServiceCatalogProvisioningArtifactDetail


class ServiceCatalogListProvisioningArtifactsResponse(BaseModel):
    ProvisioningArtifactDetails: list[ServiceCatalogProvisioningArtifactDetail] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
