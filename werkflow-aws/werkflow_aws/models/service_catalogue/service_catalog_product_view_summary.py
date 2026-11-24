from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogProductViewSummary(BaseModel):
    Id: StrictStr | None = None
    ProductId: StrictStr | None = None
    Name: StrictStr | None = None
    Owner: StrictStr | None = None
    ShortDescription: StrictStr | None = None
    Type: StrictStr | None = None
    Distributor: StrictStr | None = None
    HasDefaultPath: StrictBool | None = None
    SupportEmail: StrictStr | None = None
    SupportDescription: StrictStr | None = None
    SupportUrl: StrictStr | None = None
