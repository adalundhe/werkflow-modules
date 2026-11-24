from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class SupportDescribeCasesRequest(BaseModel):
    caseIdList: list[StrictStr] | None = None
    displayId: StrictStr | None = None
    afterTime: StrictStr | None = None
    beforeTime: StrictStr | None = None
    includeResolvedCases: StrictBool | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    language: StrictStr | None = None
    includeCommunications: StrictBool | None = None
    dryRun: StrictBool | None = None
