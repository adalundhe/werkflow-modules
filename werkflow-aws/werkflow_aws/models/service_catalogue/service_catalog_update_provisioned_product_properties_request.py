from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ServiceCatalogUpdateProvisionedProductPropertiesRequest(BaseModel):
    ProvisionedProductId: StrictStr
    ProvisionedProductProperties: dict[Literal['OWNER', 'LAUNCH_ROLE'], StrictStr]
    IdempotencyToken: StrictStr
    AcceptLanguage: StrictStr | None = None
