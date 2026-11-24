from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogProvisioningArtifactPreferences(BaseModel):
    StackSetAccounts: list[StrictStr] | None = None
    StackSetRegions: list[StrictStr] | None = None
