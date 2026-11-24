from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SSMPatch(BaseModel):
    Id: StrictStr | None = None
    ReleaseDate: datetime.datetime | StrictStr | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    ContentUrl: StrictStr | None = None
    Vendor: StrictStr | None = None
    ProductFamily: StrictStr | None = None
    Product: StrictStr | None = None
    Classification: StrictStr | None = None
    MsrcSeverity: StrictStr | None = None
    KbNumber: StrictStr | None = None
    MsrcNumber: StrictStr | None = None
    Language: StrictStr | None = None
    AdvisoryIds: list[StrictStr] | None = None
    BugzillaIds: list[StrictStr] | None = None
    CVEIds: list[StrictStr] | None = None
    Name: StrictStr | None = None
    Epoch: StrictInt | None = None
    Version: StrictStr | None = None
    Release: StrictStr | None = None
    Arch: StrictStr | None = None
    Severity: StrictStr | None = None
    Repository: StrictStr | None = None
