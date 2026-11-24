from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class IssueSecuritySchemeToProjectMapping(BaseModel):
    model_config = ConfigDict(extra="allow")

    issueSecuritySchemeId: StrictStr | None = None
    projectId: StrictStr | None = None
