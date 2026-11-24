from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ServiceCatalogProvisioningArtifactSummary(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    ProvisioningArtifactMetadata: dict[StrictStr, StrictStr] | None = None
