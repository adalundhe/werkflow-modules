from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDisassociateTagOptionFromResourceRequest(BaseModel):
    ResourceId: StrictStr
    TagOptionId: StrictStr
