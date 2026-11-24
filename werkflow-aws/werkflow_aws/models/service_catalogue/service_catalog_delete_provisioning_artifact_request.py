from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDeleteProvisioningArtifactRequest(BaseModel):
    ProductId: StrictStr
    ProvisioningArtifactId: StrictStr
    AcceptLanguage: StrictStr | None = None
