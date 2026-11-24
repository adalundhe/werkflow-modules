from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogTag(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
