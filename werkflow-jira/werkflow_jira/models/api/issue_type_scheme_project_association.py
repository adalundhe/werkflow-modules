from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeSchemeProjectAssociation(BaseModel):
    issueTypeSchemeId: StrictStr | None = None
    projectId: StrictStr | None = None
