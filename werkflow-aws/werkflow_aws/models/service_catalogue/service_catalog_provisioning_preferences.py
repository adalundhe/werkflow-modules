from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogProvisioningPreferences(BaseModel):
    StackSetAccounts: list[StrictStr] | None = None
    StackSetRegions: list[StrictStr] | None = None
    StackSetFailureToleranceCount: StrictInt | None = None
    StackSetFailureTolerancePercentage: StrictInt | None = None
    StackSetMaxConcurrencyCount: StrictInt | None = None
    StackSetMaxConcurrencyPercentage: StrictInt | None = None
