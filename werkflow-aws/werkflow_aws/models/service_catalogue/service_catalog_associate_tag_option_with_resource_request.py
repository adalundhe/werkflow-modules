from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogAssociateTagOptionWithResourceRequest(BaseModel):
    ResourceId: StrictStr
    TagOptionId: StrictStr
