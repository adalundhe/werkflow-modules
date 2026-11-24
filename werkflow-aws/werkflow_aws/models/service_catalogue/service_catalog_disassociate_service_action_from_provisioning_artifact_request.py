from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDisassociateServiceActionFromProvisioningArtifactRequest(BaseModel):
    ProductId: StrictStr
    ProvisioningArtifactId: StrictStr
    ServiceActionId: StrictStr
    AcceptLanguage: StrictStr | None = None
    IdempotencyToken: StrictStr | None = None
