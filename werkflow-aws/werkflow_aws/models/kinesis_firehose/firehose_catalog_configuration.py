from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseCatalogConfiguration(BaseModel):
    CatalogARN: StrictStr | None = None
    WarehouseLocation: StrictStr | None = None
