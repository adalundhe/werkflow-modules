from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_provisioning_artifact_detail import ServiceCatalogProvisioningArtifactDetail


class ServiceCatalogCreateProvisioningArtifactResponse(BaseModel):
    ProvisioningArtifactDetail: ServiceCatalogProvisioningArtifactDetail | None = None
    Info: dict[StrictStr, StrictStr] | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
