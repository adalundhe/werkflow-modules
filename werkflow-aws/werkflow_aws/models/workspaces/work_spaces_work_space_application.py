from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WorkSpacesWorkSpaceApplication(BaseModel):
    ApplicationId: StrictStr | None = None
    Created: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    LicenseType: StrictStr | None = None
    Name: StrictStr | None = None
    Owner: StrictStr | None = None
    State: StrictStr | None = None
    SupportedComputeTypeNames: list[StrictStr] | None = None
    SupportedOperatingSystemNames: list[StrictStr] | None = None
