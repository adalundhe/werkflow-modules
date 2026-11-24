from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeArtifactRepositorySummaryModel(BaseModel):
    name: StrictStr | None = None
    administratorAccount: StrictStr | None = None
    domainName: StrictStr | None = None
    domainOwner: StrictStr | None = None
    arn: StrictStr | None = None
    description: StrictStr | None = None
    createdTime: datetime.datetime | StrictStr | None = None
