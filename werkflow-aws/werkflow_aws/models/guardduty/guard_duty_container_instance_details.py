from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GuardDutyContainerInstanceDetails(BaseModel):
    CoveredContainerInstances: StrictInt | None = None
    CompatibleContainerInstances: StrictInt | None = None
