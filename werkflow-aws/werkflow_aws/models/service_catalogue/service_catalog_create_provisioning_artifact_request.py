from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_provisioning_artifact_properties import ServiceCatalogProvisioningArtifactProperties


class ServiceCatalogCreateProvisioningArtifactRequest(BaseModel):
    ProductId: StrictStr
    Parameters: ServiceCatalogProvisioningArtifactProperties
    IdempotencyToken: StrictStr
    AcceptLanguage: StrictStr | None = None
