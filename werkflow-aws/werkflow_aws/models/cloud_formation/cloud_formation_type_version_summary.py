from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFormationTypeVersionSummary(BaseModel):
    Type: StrictStr | None = None
    TypeName: StrictStr | None = None
    VersionId: StrictStr | None = None
    IsDefaultVersion: StrictBool | None = None
    Arn: StrictStr | None = None
    TimeCreated: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    PublicVersionNumber: StrictStr | None = None
