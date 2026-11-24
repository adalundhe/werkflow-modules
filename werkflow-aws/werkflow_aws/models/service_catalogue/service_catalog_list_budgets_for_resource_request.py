from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListBudgetsForResourceRequest(BaseModel):
    ResourceId: StrictStr
    AcceptLanguage: StrictStr | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
