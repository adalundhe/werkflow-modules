from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogListProvisioningArtifactsRequest(BaseModel):
    ProductId: StrictStr
    AcceptLanguage: StrictStr | None = None
