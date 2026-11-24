from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeArtifactDomainSummary(BaseModel):
    name: StrictStr | None = None
    owner: StrictStr | None = None
    arn: StrictStr | None = None
    status: StrictStr | None = None
    createdTime: datetime.datetime | None = None
    encryptionKey: StrictStr | None = None
