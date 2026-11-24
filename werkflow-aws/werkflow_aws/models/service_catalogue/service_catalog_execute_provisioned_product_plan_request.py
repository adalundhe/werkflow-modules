from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogExecuteProvisionedProductPlanRequest(BaseModel):
    PlanId: StrictStr
    IdempotencyToken: StrictStr
    AcceptLanguage: StrictStr | None = None
