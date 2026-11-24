from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SupportDescribeCommunicationsRequest(BaseModel):
    caseId: StrictStr
    beforeTime: StrictStr | None = None
    afterTime: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    dryRun: StrictBool | None = None
