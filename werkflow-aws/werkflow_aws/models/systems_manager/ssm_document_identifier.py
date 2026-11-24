from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_document_requires import SSMDocumentRequires
from .ssm_tag import SSMTag


class SSMDocumentIdentifier(BaseModel):
    Name: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    DisplayName: StrictStr | None = None
    Owner: StrictStr | None = None
    VersionName: StrictStr | None = None
    PlatformTypes: list[StrictStr] | None = None
    DocumentVersion: StrictStr | None = None
    DocumentType: StrictStr | None = None
    SchemaVersion: StrictStr | None = None
    DocumentFormat: StrictStr | None = None
    TargetType: StrictStr | None = None
    Tags: list[SSMTag] | None = None
    Requires: list[SSMDocumentRequires] | None = None
    ReviewStatus: StrictStr | None = None
    Author: StrictStr | None = None
    CloudProviders: list[StrictStr] | None = None
