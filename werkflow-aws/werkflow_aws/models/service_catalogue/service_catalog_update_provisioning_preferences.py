from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ServiceCatalogUpdateProvisioningPreferences(BaseModel):
    StackSetAccounts: list[StrictStr] | None = None
    StackSetRegions: list[StrictStr] | None = None
    StackSetFailureToleranceCount: StrictInt | None = None
    StackSetFailureTolerancePercentage: StrictInt | None = None
    StackSetMaxConcurrencyCount: StrictInt | None = None
    StackSetMaxConcurrencyPercentage: StrictInt | None = None
    StackSetOperationType: Literal['CREATE', 'UPDATE', 'DELETE'] | None = None
