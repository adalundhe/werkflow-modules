from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ServiceCatalogCreateProvisionedProductPlanResponse(BaseModel):
    PlanName: StrictStr | None = None
    PlanId: StrictStr | None = None
    ProvisionProductId: StrictStr | None = None
    ProvisionedProductName: StrictStr | None = None
    ProvisioningArtifactId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
