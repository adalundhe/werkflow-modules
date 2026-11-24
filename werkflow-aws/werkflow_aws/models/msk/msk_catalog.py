from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKCatalog(BaseModel):
    CatalogArn: StrictStr | None = None
    WarehouseLocation: StrictStr | None = None
