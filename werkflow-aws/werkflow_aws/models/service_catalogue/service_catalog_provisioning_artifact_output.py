from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogProvisioningArtifactOutput(BaseModel):
    Key: StrictStr | None = None
    Description: StrictStr | None = None
