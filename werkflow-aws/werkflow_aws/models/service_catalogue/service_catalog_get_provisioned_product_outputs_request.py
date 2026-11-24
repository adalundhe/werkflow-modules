from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogGetProvisionedProductOutputsRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    ProvisionedProductId: StrictStr | None = None
    ProvisionedProductName: StrictStr | None = None
    OutputKeys: list[StrictStr] | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
