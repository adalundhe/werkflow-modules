from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListServiceActionsRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
