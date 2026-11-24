from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDeleteTagOptionRequest(BaseModel):
    Id: StrictStr
