from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDescribeProvisionedProductRequest(BaseModel):
    AcceptLanguage: StrictStr | None = None
    Id: StrictStr | None = None
    Name: StrictStr | None = None
