from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ServiceCatalogUpdateProvisionedProductPropertiesResponse(BaseModel):
    ProvisionedProductId: StrictStr | None = None
    ProvisionedProductProperties: dict[StrictStr, StrictStr] | None = None
    RecordId: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
