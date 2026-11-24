from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogProvisionedProductPlanSummary(BaseModel):
    PlanName: StrictStr | None = None
    PlanId: StrictStr | None = None
    ProvisionProductId: StrictStr | None = None
    ProvisionProductName: StrictStr | None = None
    PlanType: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
