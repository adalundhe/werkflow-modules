from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGitPropertiesPatch(BaseModel):
    codeConnectionArn: StrictStr | None = None
    defaultBranch: StrictStr | None = None
