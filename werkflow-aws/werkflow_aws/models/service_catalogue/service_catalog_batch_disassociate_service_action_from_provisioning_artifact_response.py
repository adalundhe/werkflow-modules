from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .service_catalog_failed_service_action_association import ServiceCatalogFailedServiceActionAssociation


class ServiceCatalogBatchDisassociateServiceActionFromProvisioningArtifactResponse(BaseModel):
    FailedServiceActionAssociations: list[ServiceCatalogFailedServiceActionAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
