from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogStackInstance(BaseModel):
    Account: StrictStr | None = None
    Region: StrictStr | None = None
    StackInstanceStatus: StrictStr | None = None
