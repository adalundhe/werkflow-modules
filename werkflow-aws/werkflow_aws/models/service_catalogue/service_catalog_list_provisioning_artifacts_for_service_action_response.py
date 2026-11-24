from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .service_catalog_provisioning_artifact_view import ServiceCatalogProvisioningArtifactView


class ServiceCatalogListProvisioningArtifactsForServiceActionResponse(BaseModel):
    ProvisioningArtifactViews: list[ServiceCatalogProvisioningArtifactView] | None = None
    NextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
