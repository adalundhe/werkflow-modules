from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsElasticsearchDomainServiceSoftwareOptions(BaseModel):
    AutomatedUpdateDate: StrictStr | None = None
    Cancellable: StrictBool | None = None
    CurrentVersion: StrictStr | None = None
    Description: StrictStr | None = None
    NewVersion: StrictStr | None = None
    UpdateAvailable: StrictBool | None = None
    UpdateStatus: StrictStr | None = None
