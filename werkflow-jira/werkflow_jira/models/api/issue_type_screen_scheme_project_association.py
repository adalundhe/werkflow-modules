from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IssueTypeScreenSchemeProjectAssociation(BaseModel):
    issueTypeScreenSchemeId: StrictStr | None = None
    projectId: StrictStr | None = None
