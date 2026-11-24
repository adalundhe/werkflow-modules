from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListServiceActionsForProvisioningArtifactRequest(BaseModel):
    ProductId: StrictStr
    ProvisioningArtifactId: StrictStr
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
    AcceptLanguage: StrictStr | None = None
