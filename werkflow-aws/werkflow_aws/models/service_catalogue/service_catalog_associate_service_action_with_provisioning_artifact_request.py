from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogAssociateServiceActionWithProvisioningArtifactRequest(BaseModel):
    ProductId: StrictStr
    ProvisioningArtifactId: StrictStr
    ServiceActionId: StrictStr
    AcceptLanguage: StrictStr | None = None
    IdempotencyToken: StrictStr | None = None
