from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogListResourcesForTagOptionRequest(BaseModel):
    TagOptionId: StrictStr
    ResourceType: StrictStr | None = None
    PageSize: StrictInt | None = None
    PageToken: StrictStr | None = None
