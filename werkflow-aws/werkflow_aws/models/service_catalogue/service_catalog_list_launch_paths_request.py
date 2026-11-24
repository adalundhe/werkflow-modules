from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListLaunchPathsRequest(BaseModel):
    ProductId: StrictStr
    AcceptLanguage: StrictStr | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
