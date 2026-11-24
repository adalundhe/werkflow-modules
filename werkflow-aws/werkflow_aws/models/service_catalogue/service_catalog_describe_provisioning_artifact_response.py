from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_provisioning_artifact_detail import ServiceCatalogProvisioningArtifactDetail
from .service_catalog_provisioning_artifact_parameter import ServiceCatalogProvisioningArtifactParameter


class ServiceCatalogDescribeProvisioningArtifactResponse(BaseModel):
    ProvisioningArtifactDetail: ServiceCatalogProvisioningArtifactDetail | None = None
    Info: dict[StrictStr, StrictStr] | None = None
    Status: StrictStr | None = None
    ProvisioningArtifactParameters: list[ServiceCatalogProvisioningArtifactParameter] | None = None
    ResponseMetadata: dict[str, Any] | None = None
