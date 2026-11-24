from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IssueTypeToContextMapping(BaseModel):
    contextId: StrictStr | None = None
    isAnyIssueType: StrictBool | None = None
    issueTypeId: StrictStr | None = None
