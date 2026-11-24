from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogListTagOptionsFilters(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    Active: StrictBool | None = None
