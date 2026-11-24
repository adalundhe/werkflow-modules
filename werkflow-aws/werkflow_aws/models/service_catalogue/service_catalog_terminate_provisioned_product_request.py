from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogTerminateProvisionedProductRequest(BaseModel):
    TerminateToken: StrictStr
    ProvisionedProductName: StrictStr | None = None
    ProvisionedProductId: StrictStr | None = None
    IgnoreErrors: StrictBool | None = None
    AcceptLanguage: StrictStr | None = None
    RetainPhysicalResources: StrictBool | None = None
