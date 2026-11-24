from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogLaunchPath(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
