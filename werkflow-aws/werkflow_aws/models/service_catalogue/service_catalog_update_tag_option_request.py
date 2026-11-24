from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogUpdateTagOptionRequest(BaseModel):
    Id: StrictStr
    Value: StrictStr | None = None
    Active: StrictBool | None = None
