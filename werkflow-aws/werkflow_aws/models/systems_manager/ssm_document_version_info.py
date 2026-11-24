from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class SSMDocumentVersionInfo(BaseModel):
    Name: StrictStr | None = None
    DisplayName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    VersionName: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    IsDefaultVersion: StrictBool | None = None
    DocumentFormat: StrictStr | None = None
    Status: StrictStr | None = None
    StatusInformation: StrictStr | None = None
    ReviewStatus: StrictStr | None = None
    CloudProviders: list[StrictStr] | None = None
