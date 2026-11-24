from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerGetChangeLogsRequest(BaseModel):
    assessmentId: StrictStr
    controlSetId: StrictStr | None = None
    controlId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
