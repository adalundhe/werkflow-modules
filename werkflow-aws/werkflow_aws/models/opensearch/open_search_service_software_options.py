from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchServiceSoftwareOptions(BaseModel):
    CurrentVersion: StrictStr | None = None
    NewVersion: StrictStr | None = None
    UpdateAvailable: StrictBool | None = None
    Cancellable: StrictBool | None = None
    UpdateStatus: StrictStr | None = None
    Description: StrictStr | None = None
    AutomatedUpdateDate: datetime.datetime | StrictStr | None = None
    OptionalDeployment: StrictBool | None = None
