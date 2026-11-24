from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ServiceCatalogProvisioningArtifact(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    Guidance: StrictStr | None = None
