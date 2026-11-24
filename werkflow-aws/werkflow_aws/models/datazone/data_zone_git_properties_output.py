from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGitPropertiesOutput(BaseModel):
    codeConnectionArn: StrictStr | None = None
    repositoryId: StrictStr | None = None
    defaultBranch: StrictStr | None = None
    status: StrictStr | None = None
    errorMessage: StrictStr | None = None
