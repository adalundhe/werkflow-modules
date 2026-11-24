from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogProvisioningArtifactDetail(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Type: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    Active: StrictBool | None = None
    Guidance: StrictStr | None = None
    SourceRevision: StrictStr | None = None
