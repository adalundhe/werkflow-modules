from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .service_catalog_service_action_association import ServiceCatalogServiceActionAssociation


class ServiceCatalogBatchDisassociateServiceActionFromProvisioningArtifactRequest(BaseModel):
    ServiceActionAssociations: list[ServiceCatalogServiceActionAssociation]
    AcceptLanguage: StrictStr | None = None
