from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogFailedServiceActionAssociation(BaseModel):
    ServiceActionId: StrictStr | None = None
    ProductId: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
