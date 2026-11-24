from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogRecordError(BaseModel):
    Code: StrictStr | None = None
    Description: StrictStr | None = None
