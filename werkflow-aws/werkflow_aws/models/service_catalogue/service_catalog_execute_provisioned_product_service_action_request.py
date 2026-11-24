from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogExecuteProvisionedProductServiceActionRequest(BaseModel):
    ProvisionedProductId: StrictStr
    ServiceActionId: StrictStr
    ExecuteToken: StrictStr
    AcceptLanguage: StrictStr | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
