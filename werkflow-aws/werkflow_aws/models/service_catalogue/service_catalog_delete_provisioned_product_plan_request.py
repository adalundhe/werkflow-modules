from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogDeleteProvisionedProductPlanRequest(BaseModel):
    PlanId: StrictStr
    AcceptLanguage: StrictStr | None = None
    IgnoreErrors: StrictBool | None = None
