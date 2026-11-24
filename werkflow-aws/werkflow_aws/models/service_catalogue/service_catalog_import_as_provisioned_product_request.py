from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogImportAsProvisionedProductRequest(BaseModel):
    ProductId: StrictStr
    ProvisioningArtifactId: StrictStr
    ProvisionedProductName: StrictStr
    PhysicalId: StrictStr
    IdempotencyToken: StrictStr
    AcceptLanguage: StrictStr | None = None
