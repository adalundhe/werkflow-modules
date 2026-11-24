from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogServiceActionAssociation(BaseModel):
    ServiceActionId: StrictStr
    ProductId: StrictStr
    ProvisioningArtifactId: StrictStr
