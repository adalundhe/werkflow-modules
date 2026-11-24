from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogDescribeServiceActionExecutionParametersRequest(BaseModel):
    ProvisionedProductId: StrictStr
    ServiceActionId: StrictStr
    AcceptLanguage: StrictStr | None = None
