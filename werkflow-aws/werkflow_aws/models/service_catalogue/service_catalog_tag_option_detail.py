from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogTagOptionDetail(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    Active: StrictBool | None = None
    Id: StrictStr | None = None
    Owner: StrictStr | None = None
