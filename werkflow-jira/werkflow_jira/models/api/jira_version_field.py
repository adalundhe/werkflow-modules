from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JiraVersionField(BaseModel):
    versionId: StrictStr | None = None
