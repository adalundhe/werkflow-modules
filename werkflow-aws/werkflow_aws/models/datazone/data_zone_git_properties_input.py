from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGitPropertiesInput(BaseModel):
    codeConnectionArn: StrictStr
    repositoryId: StrictStr
    defaultBranch: StrictStr
